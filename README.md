# Tree data structure displayer
This program takes a level order sequence as input, builds a strict binary tree with the given input, and visually represents the tree with appropriate edge links and padding.

## Installation
To run this program, you must have Python 3 installed on your system.
- Clone this repository or download the code.
- Open a terminal and navigate to the directory where the code is located.
- Run the following command to execute the program:
`python Tree_Displayer.py`

## Usage
- Run the program as described above.
- Enter the level order sequence of the binary tree in the console.
- The program will build the tree and display it on the console.

## Example
Suppose you want to visualize the following binary tree:

```
       1
     /   \
    2     3
   / \   /  \
  4   5 6    7 
```
To represent this tree in level order sequence, we start at the root node and traverse the tree level by level, from left to right. The resulting sequence is:
```
1 2 3 4 5 6 7
```

We enter this sequence as input to the program, and it generates the following output:
```
         ┌───┐
         │ 1 │
         └─┬─┘
     ┌─────┴─────┐      
   ┌─┴─┐       ┌─┴─┐   
   │ 2 │       │ 3 │   
   └─┬─┘       └─┬─┘   
  ┌──┴──┐     ┌──┴──┐   
┌─┴─┐ ┌─┴─┐ ┌─┴─┐ ┌─┴─┐
│ 4 │ │ 5 │ │ 6 │ │ 7 │
└───┘ └───┘ └───┘ └───┘ 
```
## Contributing
If you have any suggestions for improvements or new features, feel free to submit a pull request or open an issue.

## License
This project is licensed under the MIT License - see the LICENSE.md file for details.

## Credits
The Tree-data-structure-displayer Module was developed by Valerian Coelho.
