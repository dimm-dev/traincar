# Car trainer

It is a research project for the reinforcement learning models based on a car arcade game.    
It generates random actions to train the reinforcement learning model at first 2000 ticks and then trains DQN agent after each collision with an obstacle.    
The program runs infinitely.    

DQN agent implementation is based on ['Deep Learning Illustrated'](https://www.deeplearningillustrated.com/) book's [example](https://raw.githubusercontent.com/the-deep-learners/deep-learning-illustrated/master/notebooks/cartpole_dqn.ipynb).

### Prerequisites
#### Prerequisites to run the application
Prerequisites for Linux environment (Ubuntu 20.04 package list):    
- python3-pygame    
- python3-keras    
- python3-keras-applications    
- python3-keras-preprocessing    
- python3-lasagne    

#### Development requirements
You should install Visual Studio Code in addition to the package list from the ['Prerequisites to run the application'](#running-environment) section with the following extensions:    
- ms-python.python    
- dbaeumer.vscode-eslint    

#### Packaging requirements
To make WHL package you should install packages from the ['Prerequisites to run the application'](#running-environment) section plus:    
- python3-setuptools    

To make Debian/Ubuntu (deb) packages you should install:
- python-all    
- python3-setuptools    
- python3-stdeb    
- dh-python    

### Installing
Development under Linux performs using Visual Studio Code with the 'Remote Containers' extension.
The environment is specified at .devcontainer/{devcontainer.json,Dockerfile}.    

## Running the tests
No tests yet...

## Deployment
### Build packages
1. Install packages accounted in the ['Packaging requirements'](#packaging-requirements) section.    
2. Clone source repository:
```
git clone https://github.com/dimm-dev/traincar.git
```
3. Change the working directory to traincar:
```
cd traincar
```
4. Build one of redistributable packages:    
4.1. WHL    
```
python3 setup.py bdist_wheel
```
Package will be written into `dist` subdirectory.    

4.2.DEB    
```
python3 setup.py --command-packages=stdeb.command bdist_deb
```
Package will be written into `deb_dist` subdirectory.    

### Installation
1. WHL
```
# pip3 install traincar-0.1-py3-none-any.whl
```
2. DEB
```
# dpkg -i python3-traincar_0.1-1_all.deb
```
### Running
Execute the `traincar` command from the Linux terminal or click `Games/Train Car` icon ![Train car menu icon](https://user-images.githubusercontent.com/76631698/104102741-51334100-52af-11eb-9e6d-df3737cfc264.png)
 from the applications list or system menu.   

Then you will see the infinite training process representation:    
    
![Car ride stage](https://user-images.githubusercontent.com/76631698/104065629-1f6b9d00-5211-11eb-816c-5720d5ecc1c6.png)    
The application will train the model (movement engine) and start new race after each car and obstacle collision:    

![Model traing stage](https://user-images.githubusercontent.com/76631698/104065623-1ed30680-5211-11eb-8ec9-8529aa3c91f0.png)    

## Further work

1. Pass to model only visible barriers.    
2. Change model to rectangular mode instead of plain coordinates passing.    
3. Train by human movements.    
4. Save/load model weights.    
