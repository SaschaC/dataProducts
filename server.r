
stats <- read.delim("stats.txt")
library('dplyr')
library('ggplot2')
library("rCharts")
library(plyr)

d=stats[stats$syll_n<=5,]
d$accent_p<-as.factor(d$accent_p)
levels(d$wortart)<-c("Adjective","Noun","Verb")

df<-split(d,d$wortart)
df$All<-d

function(input, output) {
  
  # Fill in the spot we created for a plot
  output$stressPlot <- renderPlot({
    ggplot(df[[input$wortart]][df[[input$wortart]][["frequency"]]>=input$min,], 
           aes(accent_p)) + geom_bar(aes(fill=syll_n))+facet_wrap(~ syll_n)+
      xlab("Stress position")+ylab("Count")+theme(legend.position="none")
    
    # Render a barplot

  })
}
