#include <boost/python.hpp>
#include "switcher.hpp"

BOOST_PYTHON_MODULE(uswitcher)
{
    using namespace boost::python;
    def("switcher", switcher);
    def("switcher_recursive", switcher_recursive);
    def("switcher2", switcher2);
    def("switcher2_recursive", switcher2_recursive);
}
