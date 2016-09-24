# Use a fluid Bootstrap layout
fluidPage(   
  
  # Give the page a title
  titlePanel("Stress position by word type and syllable number"),
  
  # Generate a row with a sidebar
  sidebarLayout(      
    
    # Define the sidebar with one input
    sidebarPanel(
      selectInput("wortart", "Word type:", 
                  choices=c("All","Adjective","Noun","Verb")),
      hr(),
      helpText("Data from CELEX corpus of German"),
    
      sliderInput("min", "Minimal word frequency:",
                  min=0, max=5000, value=1)
      
      ),
    
    # Create a spot for the barplot
    mainPanel(
      plotOutput("stressPlot")  
    )
    
  )
)
