#include"default.h"
template<typename T>
NamedObject<T>::NamedObject(const std::string& name, const T& value):name(name),value(value){}
