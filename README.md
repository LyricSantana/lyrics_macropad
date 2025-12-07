# Lyric's Macropad! :D
My custom Macropad made for Hack Club's Blueprint program! I used this project to learn how to create PCBs using KiCad and write KMK files in Python. I plan to use my Macropad for various miscellaneous tasks!

## Features:
- 5 Reprogrammable Keys
- EC11 Rotary Encoder
- 0.91" 128x32 OLED Display that can be used to display and static BMP photo!

## CAD
I used Autodesk Fusion 360 to create my case since that's what I already knew how to use!
There are two main pieces to the case: the base, which holds the PCB, and the lid, which covers most of the PCB but allows the needed parts to show.
<table>
  <tr>
    <td>Full case<br><img width="1154" height="728" alt="full" src="https://github.com/user-attachments/assets/0cb36bc9-05ec-4770-b978-a2bf54ac25d7" /></td>
  </tr>
</table>
<table>
  <tr>
    <td>Base<br><img width="1162" height="734" alt="base" src="https://github.com/user-attachments/assets/c4132cc8-34e8-4abb-898f-7f67f5f5f628" /></td>
    <td>Lid <br><img width="946" height="576" alt="newlid" src="https://github.com/user-attachments/assets/4ffc97ef-6ab2-4181-b33b-fff93b68fe75" /></td>
  </tr>
</table>


## PCB
My PCB was designed using KiCad, which was my first time using the software. 
<table>
  <tr>
    <td>Schematic<br><img width="1077" height="606" alt="schematic" src="https://github.com/user-attachments/assets/9e35cb7d-a5ca-40f6-b28e-4a4c2703a093" /></td>
    <td>PCB<br><img width="532" height="655" alt="pcb" src="https://github.com/user-attachments/assets/bf6f6776-8995-4e99-8532-fb55b8851d59" /></td>
</td>
  </tr>
</table>

## Firmware
My Macropad used KMK firmware for everything. This was my first time using this, and I wasn't able to test it while writing it, so I used a few snippets of code online for a bit of help, but most was written by me.
Here's what each key does:
- Key 1: Alt + Tab
- Key 2: CTRL + Tab
- Key 3: Mouse Middle Click
- Key 4: Alt + F4
- Key 5: Super + L
- Rotary Encoder Rotate: Volume Up/Down
- Rotary Encoder Click: Toggle Mute

## BOM
- 5x Cherry MX Switches
- 1x XIAO RP2040
- 5x Blank DSA Keycaps
- 4x M3x16 Bolt
- 4x M3 Heatset
- 1x 0.91-inch OLED display
- 1x EC11 Rotary Encoder
- Case (Lid and Base)

## Information About my Project
### Inspiration
I've always wanted a Macropad that I could program each individual component to do whatever I wanted to do. I use keybinds a LOT in most programs I use, so I hope to figure out which ones I use most and modify the code to do what I need. I added the OLED screen last minute because I wanted to add whatever silly image I wanted onto there! Overall, creating this was super fun, and I learned more than I was expecting!

### Challenges
I had previous experience with Autodesk Fusion 360, but I had never touched KiCad prior to starting this project. The learning curve was pretty steep for me, but once I got the hang of it, it was a lot better! I'm sure that there are lots of things I could have done better in my PCB design, so I would want to continue to do more research and learn best practices. Overall, it was still very fun, despite having to watch multiple tutorials for KiCad, and I learned a lot about the program!
