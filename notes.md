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