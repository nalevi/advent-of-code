#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <vector>
#include <memory>
#include <map>

struct Node
{
    std::string data;
    std::unique_ptr<Node> left;
    std::unique_ptr<Node> right;

    Node(std::string d): data(d), left(nullptr), right(nullptr) {}
};



int main()
{
    std::ifstream inpFile("input.txt");
    std::vector<std::string> rules;

    std::string rule;
    while(std::getline(inpFile, rule))
    {
        rules.push_back(rule);
    }

    inpFile.close();

    std::unique_ptr<Node> root(new Node("shiny gold"));

    std::map<std::string, std::vector<std::string>> rulesDict;

    for(auto r: rules)
    {
        std::vector<std::string> subBags;
        std::string mainBag("");
        std::string token;
        std::istringstream splitStream(r);

        
        splitStream >> token;
        mainBag = token;

        splitStream >> token;
        mainBag += " " + token;

        splitStream >> token >> token;

        while(std::getline(splitStream, token, ','))
        {
            int num;
            std::istringstream iss(token);
            std::string pattern, colour;

            iss >> num >> pattern >> colour;
            std::string subBag = pattern + " " + colour;

            subBags.push_back(subBag);
        }

        rulesDict.insert(std::make_pair(mainBag, subBags));

    }




    return 0;
}

    