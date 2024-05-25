# mistral-hackhaton

# interface

## boot

start : 

```bash
$ ./walter.sh start
```

stop : 

```bash
$ ./walter.sh stop
```

## boot (manual)

### start walter

start server in `/interface` :

```bash
$ python -m http.server 8000
```


### start whisper

download the appropriate model for the host machine :

```bash
models="tiny
tiny.en
tiny-q5_1
tiny.en-q5_1
base
base.en
base-q5_1
base.en-q5_1
small
small.en
small.en-tdrz
small-q5_1
small.en-q5_1
medium
medium.en
medium-q5_0
medium.en-q5_0
large-v1
large-v2
large-v2-q5_0
large-v3
large-v3-q5_0"
```

run in `/interface/whisper.cpp` (example: download tiny model) : 

```bash
$ bash ./models/download-ggml-model.sh tiny.en
```


whisper.cpp: run in `/interface/whisper.cpp` :

```bash
$ ./command -m ./models/ggml-tiny.en.bin -t 4
```

