#include<string>
template<typename T>
class NamedObject{
    public:
        NamedObject(const std::string& name, const T& value);
    private:
        std::string& nameValue;
        const T objectValue;
};