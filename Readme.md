# Car trainer

It is a research project for the reinforcement learning models based on a car arcade game.    
It generates random actions to train the reinforcement learning model at first 2000 ticks and then trains DQN agent after each collision with an obstacle.    
The program runs infinitely.    

DQN agent implementation is based on ['Deep Learning Illustrated'](https://www.deeplearningillustrated.com/) book's [example](https://raw.githubusercontent.com/the-deep-learners/deep-learning-illustrated/master/notebooks/cartpole_dqn.ipynb).

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

To run the application you should:
1. Install packages accounted in the ['Prerequisites'](#Prerequisites) section.    
2. Clone source repository:
```
git clone https://github.com/dimm-dev/traincar.git
```
3. Run the application from the source directory:
```
python __main__.py
```

Then you will see the infinite training process representation:  
![Car ride stage](https://user-images.githubusercontent.com/76631698/104065629-1f6b9d00-5211-11eb-816c-5720d5ecc1c6.png)    
The application will train the model (movement engine) and start new race after each car and obstacle collision:
![Model traing stage](https://user-images.githubusercontent.com/76631698/104065623-1ed30680-5211-11eb-8ec9-8529aa3c91f0.png)    


TODO:
1. deb-packages    
2. setup.py    

## Further work

1. Pass to model only visible barriers.    
2. Change model to rectangular mode instead of plain coordinates passing.    
3. Train by human movements.    
4. Save/load model weights.    
