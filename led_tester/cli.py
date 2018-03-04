# -*- coding: utf-8 -*-

"""Console script for led_tester."""
import sys
import click


@click.command()
@click.option("--input", default=None, help="input URI (file or URL)")
def main(input=None):
    """Console script for led_tester."""
    print("input", input)
    
    ''' takes two arguments from input as N and instructions, N is first number which I will use to make the
    led, i.e will be the size of the led board squared. Instructions will then be each line which will be 
    passed to the reg ex expression to have infor extracted.
    ''' 
    N, instructions = parseFile(input)
    
    ledTester = LEDtester(N)

    for instruction in instructions:
        ledTester.apply(instructions)

    print ("The amount of LED's currently "ON" is: ", ledTester.countOccuied())
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
