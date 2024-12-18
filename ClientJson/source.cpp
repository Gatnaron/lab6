#include <iostream>
#include <string>
#include "include/nlohmann/json.hpp"

using json = nlohmann::json;
using namespace std;

int main() {
    string str = R"({
        "pi": 3.141,
        "happy": true,
        "name": "Niels",
        "nothing": null,
        "answer": {
            "everything": 42
        },
        "list": [1, 0, 2],
        "object": {
            "currency": "USD",
            "value": 42.99
        }
    })";

    json j = json::parse(str);

    double pi = j["pi"];
    bool happy = j["happy"];
    string name = j["name"];

    cout << "pi: " << pi << endl;
    cout << "happy: " << happy << endl;
    cout << "name: " << name << endl;

    double value = j["object"]["value"];
    cout << "value: " << value << endl;

    cout << "everything: " << to_string(j["answer"]["everything"].get<int>()) << endl;

    for (int i = 0; i < j["list"].size(); i++) {
        cout << "list[" << i << "] = " << j["list"][i] << endl;
    }

    json j2;
    j2["num"] = 1;
    j2["array"] = json::array();
    j2["array"].push_back(1);
    j2["array"].push_back(2);
    j2["object"] = json::object();
    j2["object"].push_back({ "PI", pi });
    j2["object"].push_back({ "exp", 2.71 });

    std::cout << j2.dump(4) << endl;

    return 0;
}
