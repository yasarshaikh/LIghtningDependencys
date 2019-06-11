# LIghtningDependencys


This is an effort to find dependencies between lightning components/apps/events so that it will easy to visualize and learn the existing code in any given salesforce org. 

As of now, given code in python tries to find all the dependencies in the existing code. 

**Known Limitations:**
1. It parse code from Comments as well. Ideally comments should be not be parsed. 
2. Not tested with custom namespaces.
3. It is on premise execution. Need to make it in cloud, so that it should runtime fetches the org metadata and prepare a configuration JSON. which should fed to any visualization module. 


_Sample output is given in final_json.json file._

>>
**Future plan:**
1. Need to plug this json to some visualization libraries like - http://js.cytoscape.org/#demos or VIS js - http://visjs.org/examples/network/basicUsage.html
so that, it can be more intuitive; without much hurdles.
2. Code should be more robust, to avoid dependencies.
3. Host the app either on AWS/Heroku. Since both supports Python and other scripting languages. 
