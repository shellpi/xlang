from xerror import *

import machine
import pyb


def ledon(LED):
    try:
        LED_port = int(LED)
        port_type = 'builtin'
    except Exception:
        LED_port = LED
        port_type = 'external'

    if port_type == 'builtin':
        try:
            pyb.LED(LED_port).on()
        except Exception as e:
            panic('\nX runtime error: LED {LED_port} does not exist'.format())
    elif port_type == 'external':
        try:
            pin = machine.Pin(LED_port)
            pin(1)
        except Exception as e:
            panic('\nX runtime error: LED {LED_port} does not exist'.format())


def ledoff(LED):
    try:
        LED_port = int(LED)
        port_type = 'builtin'
    except Exception:
        LED_port = LED
        port_type = 'external'

    if port_type == 'builtin':
        try:
            pyb.LED(LED_port).off()
        except Exception as e:
            panic('\nX runtime error: LED {LED_port} does not exist'.format())
    elif port_type == 'external':
        try:
            pin = machine.Pin(LED_port)
            pin(0)
        except Exception as e:
            panic('\nX runtime error: LED {LED_port} does not exist'.format())