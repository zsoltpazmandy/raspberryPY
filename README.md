# raspberryPY
#### passtime project

##### 1. Control wrapper for the GPIO Pi-Lite dot-matrix display for the Raspberry PI
The GPIO PC-Lite display is a 14 * 9 LED-matrix one. Data is sent to the display via a 126-bit sequence iterating form the top left: vertically down on the Y axis then column by column on the X e.g.:
```
  the data (line-broken for visibility)     is displayed as follows:
   
                000000001                       00000000x00000
                000000010                       0000000x000000  
                000000100                       000000x0000000  
                000001000                       00000x00000000  
                000010000                       0000x000000000  
                000100000                       000x0000000000  
                001000000                       00x00000000000  
                010000000                       0x000000000000  
                100000000                       x0000000000000  
                000000000
                000000000
                000000000
                000000000
                000000000
```
For more easy-to-use one-off image input, therefore, a simple matrix rotation function is used: rotate once clock-wise, then mirror around the Y axis.