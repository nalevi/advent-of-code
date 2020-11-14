#include <fstream>
#include <iostream>
#include <math.h>
#include <string>
#include <vector>
#include <numeric>

int calculateFuel(int mass)
{
  return std::floor(mass/3) - 2; 
}

int calcMoreFuel(int fuel)
{
  int mf = calculateFuel(fuel);
  
  if(mf <=  0)
  {
    return fuel;    
  }
  else
  {
    fuel += calcMoreFuel(mf);
  }
  return fuel;
}

std::vector<int> fileInput(std::string file)
{
  std::ifstream inp(file);
  int mass;
  std::vector<int> inputMasses;

  while(inp >> mass )
  {
    inputMasses.push_back(mass); 
  }
  
  inp.close();
  return inputMasses;

}

int main(int argc, char* argv[])
{
  
  std::vector<int> masses = fileInput(argv[1]);
  std::vector<int> modules;

  for(auto& m: masses)
  {
     modules.push_back(calcMoreFuel(calculateFuel(m)));
  }

  long int fuelSum = std::accumulate(modules.begin(), modules.end(),0); 
   
  std::cout << "Your sum of all modules in the spacecraft: " << fuelSum << std::endl;

  return 0;
}

