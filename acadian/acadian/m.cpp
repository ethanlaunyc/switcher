#include <boost/python.hpp>
#include "switcher.hpp"

BOOST_PYTHON_MODULE(uswitcher)
{
    using namespace boost::python;
    def("switcher", switcher);
}
