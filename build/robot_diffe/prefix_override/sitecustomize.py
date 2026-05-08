import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/manuel2404/pascalito_turing_robotics/install/robot_diffe'
