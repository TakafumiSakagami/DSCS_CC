# DSCS_CC

Costume Creator for Digimon Story: Cyber Sleuth.

## Dependencies
- PyQt5
- [DSCSRenderer](https://github.com/Pherakki/DSCSRenderer) [Included with repository]
- A C++ compiler

## Building Instructions
### Setting up Dependencies
1) If you do not have PyQt5 installed, you can obtain it by running `pip install PyQt5`.
2) In the root repository directory, run `python setup.py build_ext --inplace`. This will compile the dependency `DSCSRenderer` and move the library to the root repository directory.

### Building the program to an executable file
You can build the program itself to an executable file with Nuitka. Nuitka can be installed as a Python package with `pip install Nuitka`. On Windows, the command to build is

`nuitka CostumeEditor.py --show-progress --standalone --plugin-enable=qt-plugins --windows-disable-console`

Note that most of the binaries that will be copied to the build directory are not necessary for the program to function. Official releases should contain only the necessary binaries.
