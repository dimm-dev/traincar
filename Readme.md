# Car trainer

It is a research project for the reinforcement learning models based on a car arcade game.

### Prerequisites

Prerequisites for Linux environment (Ubuntu 20.04 package list):    
- python3-pygame    
- python3-keras    
- python3-keras-applications    
- python3-keras-preprocessing    
- python3-lasagne    

Visual Studio Code extensions:    
- ms-python.python    
- dbaeumer.vscode-eslint    

### Installing

Development under Linux performs using Visual Studio Code with the 'Remote Containers' extension.
The environment is specified at .devcontainer/{devcontainer.json,Dockerfile}.    

## Running the tests

No tests yet...

## Deployment

To run application you should:
1. Install packages accounted in the ['Prerequisites'](#Prerequisites) section.    
2. Clone source repository:
```
git clone https://github.com/dimm-dev/traincar.git
```
3. Run application from the source directory:
```
python __main__.py
```

TODO:
- deb-packages    
- setup.py

## Further work

1. Change model to rectangular mode instead of plain coordinates passing.    
