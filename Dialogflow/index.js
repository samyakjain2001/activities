// See https://github.com/dialogflow/dialogflow-fulfillment-nodejs
// for Dialogflow fulfillment library docs, samples, and to report issues
'use strict';
 
const functions = require('firebase-functions');
const {WebhookClient} = require('dialogflow-fulfillment');
const {Card, Suggestion} = require('dialogflow-fulfillment');
const axios = require('axios'); 

process.env.DEBUG = 'dialogflow:debug'; // enables lib debugging statements
 
exports.dialogflowFirebaseFulfillment = functions.https.onRequest((request, response) => {
  const agent = new WebhookClient({ request, response });
  console.log('Dialogflow Request headers: ' + JSON.stringify(request.headers));
  console.log('Dialogflow Request body: ' + JSON.stringify(request.body));
 
  function welcome(agent) {
    agent.add(`Welcome to my agent!`);
  }
 
  function fallback(agent) {
    agent.add(`I didn't understand`);
    agent.add(`I'm sorry, can you try again?`);
  }
  
  function updateDataInSheet(agent) {
    const {
      Name, Email, Date, TopicsCovered, RepoLink
    } = agent.parameters;
    /*const data = {
      "Name" : Name,
      "Email" : Email,
      "Date" : Date,
      "TopicsCovered" : TopicsCovered,
      "RepoLink" : RepoLink,
      "UpdatedAt" : new Date()
    }; */
    
    agent.add("Response from inline editor: "+ Email);
    let url = "https://sheetdb.io/api/v1/y8w6eqs0oazor?sheet=Sheet1";
    return new Promise( (resolve, reject) => {
            axios.post(url, {
        "data": {
                "Name" : Name,
                  "Email" : Email,
                  "Date" : Date,
                  "RepoLink" : RepoLink,
                  "TopicsCovered" : TopicsCovered,
        }});
    }
    );
  }
  function getWeather(agent){
    const {city, date} = agent.parameters;
    let newdate = new Date(date);
    let month = newdate.getMonth();
    let day = newdate.getDate();
    let appKey = '99db9c79508a8f4717a84ead833267f7';
    let desc = "";
    let url = `https://api.openweathermap.org/data/2.5/forecast?q=${city}&appid=${appKey}&units=metric`;
    
    return new Promise( (resolve, reject) => {
      axios.post(url).then(function(res) {
      	let obj = JSON.parse(res);
        let list = obj.list;
        
        for(let i= 0; i<obj.list.length; i++){
          let date = new Date(obj.list[i].dt *1000);
          if(date.getDate()== day && date.getMonth()==month){
            desc += obj.list[i].weather[0].description;
    		agent.add("Weather for "+city+" on "+date+" is: "+desc);
            break;
          }
        }
      agent.add("DateString, day, month, listLength: "+ newdate);
      });
    });
    agent.add("newdate, day, month: "+ newdate);
    
  }
  
  // Run the proper function handler based on the matched Dialogflow intent name
  let intentMap = new Map();
  intentMap.set('Default Welcome Intent', welcome);
  intentMap.set('Default Fallback Intent', fallback);
  intentMap.set('WorkStatus', updateDataInSheet);
  intentMap.set('GetWeather', getWeather);
  // intentMap.set('your intent name here', googleAssistantHandler);
  agent.handleRequest(intentMap);
});
