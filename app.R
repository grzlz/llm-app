library(shiny)
library(httr)
library(jsonlite)

ui <- fluidPage(
  tags$head(
    tags$style(HTML("
      .container-fluid {
        padding: 0;
      }
      
      .inputs{
        margin: 20px;
      }
      
      body {
        background-color: white;
      }
      
      .header {
        background-color: #87F1FF;
        padding: 20px;
        margin: 0;
        display: flex;
        align-items: left;
        margin-bottom: 20px;
        color: #212661;
      }
      .header img {
        margin-right: 20px;
      }
      .submit, .fetch {
        margin: 20px;
      }
      .fetch {
        position: absolute;
        right: 10px;
      }
      .graphs {
        padding: 20px;
        margin: 20px;
        background-color: #6B6054;
        display: flex;
        flex-direction: column;
      }
      .graph1, .graph2 {
        background-color: white;
        padding: 20px;
        width: 90%;
        margin: 20px;
      }
      
      .table1 {
        width: 100%;
        margin: 20px auto;  # center table
      }
      
      .table1 .shiny-table-output {
        background-color: #6B6054;  # same as .graphs
        }
      
      @media (min-width: 768px) {
        .graphs {
          flex-direction: row;
        }
        .graph1, .graph2, .table1 {
          width: 50%;
        }
      }
      
      
      
      h2 {
        margin-top: 30px;
        
      }
    "))
  ),
  div(class = "header",
      img(src = "logo.png", height = "80px"),  # Replace 'logo.png' with the path to your logo image
      h2("Sentiment analysis")  # Replace 'Company Name' with the actual company name
  ),
  div(class = "inputs", 
  fileInput("file1", "Sube un archivo",
            accept = c(
              "text/csv",
              "text/comma-separated-values,text/plain",
              ".csv"))   
  ),
  actionButton("submit", "Aceptar", class = "submit"),
  actionButton("fetch", "Recolectar datos", class = "fetch"),
  div(class = "graphs",
      div(class = "graph1", plotOutput("plot1")),
      div(class = "graph2", plotOutput("plot2"))
  ),
  div(class = "table1", tableOutput("contents"))
)

server <- function(input, output) {
  observeEvent(input$submit, {
    req(input$file1)
    
    # Upload the file to the FastAPI endpoint
    res <- POST("http://localhost:5000/uploadcsv/", body = list(file = upload_file(input$file1$datapath[1])))
    
    # Check the response
    if (res$status_code == 200) {
      print("File uploaded successfully")
      data <- read.csv(input$file1$datapath[1])
      output$contents <- renderTable({
        data
      })
      
    } else {
      print("Failed to upload file")
    }
  })
  
  observeEvent(input$fetch, {
    # Get the processed data from the API
    res <- GET("http://localhost:5000/data/")
    
    # Check the response
    if (res$status_code == 200) {
      print("Data retrieved successfully")
      # Parse JSON response
      data <- content(res, "text")  # Get the response content as text
      df <- fromJSON(data)          # Convert JSON to a data frame
      
      # Rename columns if needed
      colnames(df) <- c("provider", "product", "sentiment_score")
      
      # Print the resulting dataframe
      print(df)

      #output$contents <- renderTable({
       # print(table_data)
        #colnames(table_data) <- c("Opiniones de clientes", colnames(table_data)[-1])
        #table_data
      #})
      output$plot1 <- renderPlot({
        plot(10:1)
      })
    } else {
      print("Failed to retrieve data")
    }
  })
  
  output$plot1 <- renderPlot({
    # Replace this with the code to generate your first plot
    plot(1:10)
  })
  
  output$plot2 <- renderPlot({
    # Replace this with the code to generate your second plot
    plot(10:1)
  })

  
  
  
}

shinyApp(ui = ui, server = server)
