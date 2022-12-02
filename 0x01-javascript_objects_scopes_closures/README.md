# Javascript - Objects, Scopes and Closures

In this second Holberton JavaScript project I dived into the infamously fun aspects of the language - scope, closures and  `this`. I practiced working with objects and ES6-style classes.



## [](https://github.com/bdbaraban/holbertonschool-higher_level_programming#function-prototypes-floppy_disk)Function Prototypes  💾

Prototypes for functions written in this project:

File

Prototype

`7-occurrences.js`

`exports.nbOccurences = function (list, searchElement)`

`8-esrever.js`

`exports.esrever = function (list)`

`9-logme.js`

`exports.logMe = function (item)`

`10-converter.js`

`exports.converter = function (base)`

## [](https://github.com/bdbaraban/holbertonschool-higher_level_programming#tasks-page_with_curl)Tasks  📃

-   **0. Rectangle #0**
    
    -   [0-rectangle.js](https://github.com/bdbaraban/holbertonschool-higher_level_programming/blob/master/0x13-javascript_objects_scopes_closures/0-rectangle.js): JavaScript script that defines an empty class  `Rectangle`.
-   **1. Rectangle #1**
    
    -   [1-rectangle.js](https://github.com/bdbaraban/holbertonschool-higher_level_programming/blob/master/0x13-javascript_objects_scopes_closures/1-rectangle.js): JavaScript script that defines a class  `Rectangle`. Builds on  [0-rectangle.js](https://github.com/bdbaraban/holbertonschool-higher_level_programming/blob/master/0x13-javascript_objects_scopes_closures/0-rectangle.js)  with:
        -   Constructor that initializes instance attributes  `width`  and  `height`  with given parameters  `w`  and  `h`.
-   **2. Rectangle #2**
    
    -   [2-rectangle.js](https://github.com/bdbaraban/holbertonschool-higher_level_programming/blob/master/0x13-javascript_objects_scopes_closures/2-rectangle.js): JavaScript script that defines a class  `Rectangle`. Builds on  [1-rectangle.js](https://github.com/bdbaraban/holbertonschool-higher_level_programming/blob/master/0x13-javascript_objects_scopes_closures/1-rectangle.js)  with:
        -   If provided  `w`  and  `h`  are less than or equal to  `0`, creates an empty object.
-   **3. Rectangle #3**
    
    -   [3-rectangle.js](https://github.com/bdbaraban/holbertonschool-higher_level_programming/blob/master/0x13-javascript_objects_scopes_closures/3-rectangle.js): JavaScript script that defines a class  `Rectangle`. Builds on  [3-rectangle.js](https://github.com/bdbaraban/holbertonschool-higher_level_programming/blob/master/0x13-javascript_objects_scopes_closures/3-rectangle.js)  with:
        -   Instance method  `print()`  that prints the rectangle using the  `X`  character.
-   **4. Rectangle #4**
    
    -   [4-rectangle.js](https://github.com/bdbaraban/holbertonschool-higher_level_programming/blob/master/0x13-javascript_objects_scopes_closures/4-rectangle.js): JavaScript script that defines a class  `Rectangle`. Builds on  [4-rectangle.js](https://github.com/bdbaraban/holbertonschool-higher_level_programming/blob/master/0x13-javascript_objects_scopes_closures/4-rectangle.js)  with:
        -   Instance method  `rotate()`  that swaps the  `width`  and  `height`  of the  `Rectangle`.
        -   Instance method  `double()`  that multiplies the  `width`  and  `height`  of the  `Rectangle`  by  `2`.
-   **5. Square #0**
    
    -   [5-square.js](https://github.com/bdbaraban/holbertonschool-higher_level_programming/blob/master/0x13-javascript_objects_scopes_closures/5-square.js): JavaScript script that defines a class  `Square`  that inherits from  `Rectangle`.
        -   Constructor takes one argument  `size`.
-   **6. Square #1**
    
    -   [6-square.js](https://github.com/bdbaraban/holbertonschool-higher_level_programming/blob/master/0x13-javascript_objects_scopes_closures/6-square.js): JavaScript script that defines a class  `Square`  that inherits from  `Rectangle`. Builds on  [5-square.js](https://github.com/bdbaraban/holbertonschool-higher_level_programming/blob/master/0x13-javascript_objects_scopes_closures/5-square.js)  with:
        -   Instance method  `charPrint(c)`  that prints the  `Square`  using the character  `c`.
        -   If  `c`  is  `undefined`, uses the character  `X`.
-   **7. Occurrences**
    
    -   [7-occurrences.js](https://github.com/bdbaraban/holbertonschool-higher_level_programming/blob/master/0x13-javascript_objects_scopes_closures/7-occurrences.js): JavaScript function that returns the number of occurrences in a list.
-   **8. Esrever**
    
    -   [8-esrever.js](https://github.com/bdbaraban/holbertonschool-higher_level_programming/blob/master/0x13-javascript_objects_scopes_closures/8-esrever.js): JavaScript function that reverses a list.
-   **9. Log me**
    
    -   [9-logme.js](https://github.com/bdbaraban/holbertonschool-higher_level_programming/blob/master/0x13-javascript_objects_scopes_closures/9-logme.js): JavaScript function that prints the number of arguments already printed as well as the new argument value.
    -   Output:  `<number arguments already printed>: <current argument value>`
-   **10. Number conversion**
    
    -   [10-converter.js](https://github.com/bdbaraban/holbertonschool-higher_level_programming/blob/master/0x13-javascript_objects_scopes_closures/10-converter.js): JavaScript function that converts a number from base 10 to another base passed as argument.