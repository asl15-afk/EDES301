"""
---------------------------------------------------------------------------------------
USR3 LED Blink Program
---------------------------------------------------------------------------------------
Author: Alexis Leyow (asl@rice.edu)
Last Modified: 10/07/2025

License:

Copyright 2025 - Alexis Leyow

Redistribution and use in source and binary forms, with or without 
modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this 
list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice, 
this list of conditions and the following disclaimer in the documentation and/or other 
materials provided with the distribution.

3. Neither the name of the copyright holder nor the names of its contributors may 
be used to endorse or promote products derived from this software without specific prior 
written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS “AS IS” AND ANY EXPRESS 
OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF 
MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL 
THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, 
EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE 
GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY 
THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) 
ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

MIT License

Copyright (c) 2019 Jason Kridner

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
---------------------------------------------------------------------------------------
This Python program uses the Adafruit_BBIO library to control the PocketBeagle’s
onboard USR3 LED. The LED is toggled ON and OFF at a rate of 5 Hz, which means
it completes five full blink cycles per second (0.1 seconds ON, 0.1 seconds OFF).
The Adafruit_BBIO.GPIO module provides a simple interface for configuring and
manipulating the BeagleBone and PocketBeagle’s GPIO pins. In this program, USR3
is configured as a GPIO output. Inside an infinite loop, the LED state alternates
between HIGH (on) and LOW (off), with a short delay in between, producing the
visible blinking effect.
"""
import Adafruit_BBIO.GPIO as GPIO
import time

LED = "USR3"
GPIO.setup(LED, GPIO.OUT)

try:
    print("Blinking USR3 at 5 Hz. Press Ctrl+C to stop.")
    while True:
        GPIO.output(LED, GPIO.HIGH)
        time.sleep(0.1)
        GPIO.output(LED, GPIO.LOW)
        time.sleep(0.1)
except KeyboardInterrupt:
    GPIO.output(LED, GPIO.LOW)
    GPIO.cleanup()
    print("\nStopped blinking.")