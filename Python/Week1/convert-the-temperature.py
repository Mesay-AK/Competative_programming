class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        Kelvin = celsius + 273.15
        Fahrenheit = celsius * 1.80 + 32.00
        result=[]
        result.append(Kelvin)
        result.append(Fahrenheit)
        return result
