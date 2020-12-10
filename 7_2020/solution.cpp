#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <vector>
#include <memory>
#include <map>
#include <algorithm>


class SearchTree
{
    private:
        struct Node
        {
            std::string data;
            std::shared_ptr<Node> parent;
            std::vector<std::shared_ptr<Node>> children;

            Node(std::string d): data(d), parent(nullptr) {}
        };

        std::shared_ptr<Node> _root;
        int _height;
    public:
        SearchTree(std::string rootData): _root(new Node(rootData)), _height(0) {}
        ~SearchTree() 
        { 
            _root->children.clear();
        }

        void push(std::string data);

        int getHeight() { return _height; }
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

    SearchTree st("shiny gold");

    for(auto b: rulesDict)
    {
        ;
    }



    return 0;
}

    
void SearchTree::push(std::string data)
{
    if(_root->children.size() == 0 || std::find(_root->children.begin(),_root->children.end(), std::shared_ptr<Node>(new Node(data))) == _root->children.end())
    {
        std::shared_ptr<Node> newNode(new Node(data));
        newNode->parent = _root;
        _root->children.push_back(std::move(newNode));
    }
    else
    {
        
    } 
}