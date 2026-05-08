# buho_turing_robotics
# Pascalito Turing Robotics

Workspace ROS 2 Jazzy para simulación y desarrollo de robots móviles.

## Requisitos

- Ubuntu 24.04
- ROS 2 Jazzy
- Gazebo Harmonic

## Clonar el repositorio o hacer pull para bajar lo nuevo

```bash
git clone https://github.com/ManuelOrtizCamacho/pascalito_turing_robotics.git
```

## Entrar al workspace

```bash
cd pascalito_turing_robotics
```

## Instalar dependencias

```bash
sudo apt update

sudo apt install -y \
  ros-jazzy-ros-gz \
  ros-jazzy-ros-gz-bridge \
  ros-jazzy-joint-state-publisher \
  ros-jazzy-xacro \
  ros-jazzy-teleop-twist-keyboard \
  ros-jazzy-teleop-twist-joy
```

## Compilar el workspace

```bash
source /opt/ros/jazzy/setup.bash

colcon build --symlink-install
```

## Cargar el workspace

```bash
source install/setup.bash
```

## Ejecutar la simulación

```bash
ros2 launch gazebo_differential_drive_robot robot.launch.py
```

## Control por teclado

Abrir otra terminal:

```bash
source /opt/ros/jazzy/setup.bash

source ~/pascalito_turing_robotics/install/setup.bash

ros2 run teleop_twist_keyboard teleop_twist_keyboard
```

## Estructura del workspace

```text
pascalito_turing_robotics/
├── src/
├── build/
├── install/
├── log/
```
