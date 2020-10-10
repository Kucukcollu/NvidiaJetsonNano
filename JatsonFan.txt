## Nvidia Jetson Nano Fan Settings

#### Used fan has 4 pin.

#### At first, we should notice that frome latest updates, the fan will work after a specific temperature as default.

#### But you can run the fun with this setting via adjusting the speed,etc.


`$sudo jetson_clocks`

`$sudo jetson_clocks --store`

`$sudo gedit l4t_dfs.conf`

    --> target_pwm: 255
    --> temp_control: 0

    then save end exit.

`$sudo jetson_clocks --restore`
