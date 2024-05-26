whisper command

* i included drogon
* drogon needs a compiler that supports c++17
* "For GCC, version 7 or higher is required. For Clang, version 4 or higher should suffice."

changed in makefile:
```
# CXXFLAGS = -I. -I./examples -O3 -DNDEBUG -std=c++11 -fPIC
CXXFLAGS = -I. -I./examples -O3 -DNDEBUG -std=c++17 -fPIC

```

// window.loadFileFromBackend = function(pdbfile) {
          //   if (stage && pdbfile) {
          //     stage.loadFile(pdbfile, {defaultRepresentation: true}).then(function(component) {
          //       console.log('Backend file loaded successfully');
          //     }).catch(function(error) {
          //       console.error('Error loading backend file:', error);
          //     });
          //   }
          // }


fastapi main endpoint (test, ip will change):

curl -X POST "http://51.159.183.152:8000/predict" \
-H "Content-Type: application/json" \
-d '{
  "prompt": "What is the capital of France?",
  "max_tokens": 256,
  "temperature": 1.0
}'


if (data.sdfFile) {                
    handleFileLoad(data.sdfFile);  
}

curl -X POST "http://51.159.183.152:8000/predict" -F "testing" -F "max_tokens=256" -F "temperature=1.0" -F "file=@./5uak.pdb"



