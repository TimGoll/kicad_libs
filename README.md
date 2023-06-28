# KiCAD Libraries - Symbols and Footprints

This library contains an assortment of symbols and footprints used in my KiCAD designs. The footprints do not contain any 3D models used in the 3D viewer.

## Symbols

All symbols are located within the [TimGollLin.kicad_sym](./TimGollLib.kicad_sym) file.

### AD817

<img src="assets/AD817.svg" align="right" height="120px">

The AD817 is a low cost, low power, single/dual supply, high speed op amp which is ideally suited for a broad spectrum of signal conditioning and data acquisition applications.

**Datasheet:** https://www.analog.com/media/en/technical-documentation/data-sheets/AD817.pdf

## Footprints

### Tie Hook

A basic tie hook that can be used to connect an oscilloscope probe or as a hook for an cable tie. It is modeled after [this hook](https://jlcpcb.com/partdetail/Ronghe-RH5019/C5199800).

![tie hook rendering](assets/tie-hook.png)

### LDD-700LS

An off the shelf 700mA LED driver package by Meanwell.

![LDD 700LS rendering](assets/ldd-700ls.png)
[[external 3d model source]](https://ms.componentsearchengine.com/detail.html?searchString=LDD-700LS&manuf=Mean%20Well&country=GB&language=en&source=1)

### Generic LED XSSY 3.9x3.9

A generic footprint for XSSY SMD LEDs.

![LED XSSY footprint rendering](assets/LED_XSSY_3.9x3.9.png)

### OLED 128x64 ZIF connector

A footprint for an OLED display with ZIF connector [like this one](https://www.buydisplay.com/blue-128x64-0-96-inch-oled-display-top-contact-connector-fpc-ssd1306).

![oled rendering](assets/oled_128x64_zif.png)
[[3d model file]](3d_model_source/128x64_oled_display_1.6mm.FCStd)

### TC2030

Footprint for a [TagConnect 2030](https://www.tag-connect.com/product/tc2030-ctx-stdc14-for-use-with-stm32-processors-with-stlink-v3) programming port on the PCB.

![TC2030 rendering](assets/tc2030.png)