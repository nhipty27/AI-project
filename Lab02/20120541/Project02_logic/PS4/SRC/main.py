import os
from PL_Resolution import resolution
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_INPUT=ROOT_DIR+'\INPUT'
ROOT_OUTPUT=ROOT_DIR+'\OUTPUT'

def main():
    for file in os.listdir(ROOT_INPUT):
        solution = resolution()
        solution.initSolution(file)
        file_output='output'+ file[file.find('input') + 5:]
        # solution.PL_RESOLUTION()
        solution.outputSolution(file_output)

if __name__ == '__main__':
    main()