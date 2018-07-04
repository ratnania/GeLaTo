# coding: utf-8

from sympy.core.containers import Tuple
from sympy import symbols

from gelato.calculus import dx, dy, dz
from gelato.calculus import Constant
from gelato.calculus import Field
from gelato.calculus import grad, dot, inner, cross, rot, curl, div

from gelato.fem.core import FemSpace
from gelato.fem.core import TestFunction
from gelato.fem.core import TrialFunction
from gelato.fem.core import VectorTestFunction
from gelato.fem.core import VectorTrialFunction
from gelato.fem.core import DerivativeSymbol
from gelato.fem.expr import BilinearForm
from gelato.fem.expr import gelatize, normalize_weak_from


# ...
def test_bilinear_form_2d_0():
    print('============ test_bilinear_form_2d_0 =============')

    W = FemSpace('W', ldim=2)
    V = FemSpace('V', ldim=2)

    w = TestFunction(W, name='w')
    v = TrialFunction(V, name='v')

    a = BilinearForm(inner(grad(w), grad(v)), trial_space=V, test_space=W)
    b = BilinearForm(w*v, trial_space=V, test_space=W)

    c = a + b
    print('> input         >>> {0}'.format(c))
    print('> gelatized     >>> {0}'.format(gelatize(c)))
    print('> normal form   >>> {0}'.format(normalize_weak_from(c)))
    print('')

    v1 = TestFunction(V, name='v1')
    u1 = TrialFunction(W, name='u1')

    d = a(v1, u1) + b
    print('> input         >>> {0}'.format(d))
    print('> gelatized     >>> {0}'.format(gelatize(d)))
    print('> normal form   >>> {0}'.format(normalize_weak_from(d)))
    print('')
# ...

# ...
def test_bilinear_form_2d_1():
    print('============ test_bilinear_form_2d_1 =============')

    W = FemSpace('W', ldim=2)
    V = FemSpace('V', ldim=2)

    w = TestFunction(W, name='w')
    v = TrialFunction(V, name='v')

    expr = inner(grad(w), grad(v))

    a = BilinearForm(expr, trial_space=V, test_space=W)
    print('> input         >>> {0}'.format(a))
    print('> gelatized     >>> {0}'.format(gelatize(a)))
    print('> normal form   >>> {0}'.format(normalize_weak_from(a)))
    print('')
# ...

# ...
def test_bilinear_form_2d_2():
    print('============ test_bilinear_form_2d_2 =============')

    W = FemSpace('W', ldim=2)
    V = FemSpace('V', ldim=2)

    w = TestFunction(W, name='w')
    v = TrialFunction(V, name='v')

    expr = cross(curl(w), curl(v)) + 0.2 * w * v

    a = BilinearForm(expr, trial_space=V, test_space=W)
    print('> input         >>> {0}'.format(a))
    print('> gelatized     >>> {0}'.format(gelatize(a)))
    print('> normal form   >>> {0}'.format(normalize_weak_from(a)))
    print('')
# ...

# ...
def test_bilinear_form_2d_3():
    print('============ test_bilinear_form_2d_3 =============')

    W = FemSpace('W', ldim=2)
    V = FemSpace('V', ldim=2)

    w = TestFunction(W, name='w')
    v = TrialFunction(V, name='v')

    bx = Constant('bx')
    by = Constant('by')
    b = Tuple(bx, by)

    expr = 0.2 * w * v + dot(b, grad(v)) * w

    a = BilinearForm(expr, trial_space=V, test_space=W)
    print('> input         >>> {0}'.format(a))
    print('> gelatized     >>> {0}'.format(gelatize(a)))
    print('> normal form   >>> {0}'.format(normalize_weak_from(a)))
    print('')
# ...

# ... TODO debug
def test_bilinear_form_2d_4():
    print('============ test_bilinear_form_2d_4 =============')

    W = FemSpace('W', ldim=2, is_vector=True, shape=2)
    V = FemSpace('V', ldim=2, is_vector=True, shape=2)

    w = VectorTestFunction(W, name='w')
    v = VectorTrialFunction(V, name='v')

    expr = rot(w) * rot(v) + div(w) * div(v) #+ 0.2 * dot(w, v)

    a = BilinearForm(expr, trial_space=V, test_space=W)
    print('> input         >>> {0}'.format(a))
    print('> gelatized     >>> {0}'.format(gelatize(a)))
    print('> normal form   >>> {0}'.format(normalize_weak_from(a)))
    print('')
# ...


# .....................................................
if __name__ == '__main__':
    test_bilinear_form_2d_0()
    test_bilinear_form_2d_1()
    test_bilinear_form_2d_2()
    test_bilinear_form_2d_3()
#    test_bilinear_form_2d_4()