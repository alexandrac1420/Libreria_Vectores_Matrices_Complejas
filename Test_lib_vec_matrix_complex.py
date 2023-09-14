import unittest
import vec_matrix_complex as lb
import numpy as np
import math
class TestLibMatrixComplex(unittest.TestCase):
    v1 = [complex(3.5, 2.35), complex(1.78, -8.25)]
    v2 = [complex(-1.8, 2.5), complex(2.78, 3.2)]
    v3 = [complex(-3, -2.1), complex(1.5, -8.0)]

    def test_sum_vec(self):
        prueba_1 = lb.sum_vec_complex(self.v1,self.v2)
        self.assertAlmostEqual(prueba_1[0], complex(1.7, 4.85))
        self.assertAlmostEqual(prueba_1[1], complex(4.56,-5.05))
        prueba_2 = lb.sum_vec_complex(self.v2,self.v3)
        self.assertAlmostEqual(prueba_2[0], complex(-4.8,0.4))
        self.assertAlmostEqual(prueba_2[1], complex(4.28,-4.8))

    def test_inv_vec(self):
        prueba_1 = lb.inv_vec_complex(self.v1)
        self.assertAlmostEqual(prueba_1[0],complex(-3.5,-2.35))
        self.assertAlmostEqual(prueba_1[1],complex(-1.78,8.25))
        prueba_2 = lb.inv_vec_complex(self.v2)
        self.assertAlmostEqual(prueba_2[0],complex(1.8,-2.5))
        self.assertAlmostEqual(prueba_2[1],complex(-2.78,-3.2))

    def test_mult_vec(self):
        prueba_1 = lb.mult_esc_vec(2, self.v1)
        self.assertAlmostEqual(prueba_1[0], complex(7,4.7))
        self.assertAlmostEqual(prueba_1[1], complex(3.56,-16.5))
        prueba_2 = lb.mult_esc_vec(-3, self.v2)
        self.assertAlmostEqual(prueba_2[0], complex(5.4,-7.5))
        self.assertAlmostEqual(prueba_2[1], complex(-8.34,-9.6))

    m1 = np.array([[complex(3.5,2.8), complex(1.5,-8.2)], [complex(1.5,2.8), complex(2.7,3.25)]])
    m2 = np.array([[complex(-1.25,5.15), complex(1.2,3.70)], [complex(1.2,2.78), complex(1.7, -1.78)]])
    m3 = np.array([[complex(8.7,2.1), complex(1.1,-8.2)], [complex(1.7,-5.5), complex(-2,-3)]])

    def test_sum_matrix(self):
        prueba_1 = lb.sum_matrix(self.m1, self.m2)
        self.assertAlmostEqual(prueba_1[0][0], complex(2.25,7.95))
        self.assertAlmostEqual(prueba_1[0][1], complex(2.7,-4.5))
        self.assertAlmostEqual(prueba_1[1][0], complex(2.7,5.58))
        self.assertAlmostEqual(prueba_1[1][1], complex(4.4,1.47))
        prueba_2 = lb.sum_matrix(self.m2, self.m3)
        self.assertAlmostEqual(prueba_2[0][0], complex(7.45,7.25))
        self.assertAlmostEqual(prueba_2[0][1], complex(2.3,-4.5))
        self.assertAlmostEqual(prueba_2[1][0], complex(2.9,-2.72))
        self.assertAlmostEqual(prueba_2[1][1], complex(-0.3,-4.78))

    def test_inv_matrix(self):
        prueba_1 = lb.inv_matrix(self.m1)
        self.assertAlmostEqual(prueba_1[0][0], complex(-3.5,-2.8))
        self.assertAlmostEqual(prueba_1[0][1], complex(-1.5,8.2))
        self.assertAlmostEqual(prueba_1[1][0], complex(-1.5,-2.8))
        self.assertAlmostEqual(prueba_1[1][1], complex(-2.7,-3.25))
        prueba_2 = lb.inv_matrix(self.m2)
        self.assertAlmostEqual(prueba_2[0][0], complex(1.25,-5.15))
        self.assertAlmostEqual(prueba_2[0][1], complex(-1.2,-3.70))
        self.assertAlmostEqual(prueba_2[1][0], complex(-1.2,-2.78))
        self.assertAlmostEqual(prueba_2[1][1], complex(-1.7,1.78))

    def test_mult_scalar_matrix(self):
        prueba_1 = lb.mult_esca_matrix(2, self.m1)
        self.assertAlmostEqual(prueba_1[0][0], complex(7,5.6))
        self.assertAlmostEqual(prueba_1[0][1], complex(3,-16.4))
        self.assertAlmostEqual(prueba_1[1][0], complex(3,5.6))
        self.assertAlmostEqual(prueba_1[1][1], complex(5.4,6.5))
        prueba_2 = lb.mult_esca_matrix(-3,self.m2)
        self.assertAlmostEqual(prueba_2[0][0], complex(3.75,-15.45))
        self.assertAlmostEqual(prueba_2[0][1], complex(-3.6,-11.1))
        self.assertAlmostEqual(prueba_2[1][0], complex(-3.6,-8.34))
        self.assertAlmostEqual(prueba_2[1][1], complex(-5.1,5.34))

    def test_trans_matrix(self):
        prueba_1 = lb.trans_matrix(self.m1)
        self.assertAlmostEqual(prueba_1[0][0], complex(3.5,2.8))
        self.assertAlmostEqual(prueba_1[0][1], complex(1.5,2.8))
        self.assertAlmostEqual(prueba_1[1][0], complex(1.5,-8.2))
        self.assertAlmostEqual(prueba_1[1][1], complex(2.7,3.25))
        prueba_2 = lb.trans_matrix(self.m2)
        self.assertAlmostEqual(prueba_2[0][0], complex(-1.25,5.15))
        self.assertAlmostEqual(prueba_2[0][1], complex(1.2,2.78))
        self.assertAlmostEqual(prueba_2[1][0], complex(1.2,3.70))
        self.assertAlmostEqual(prueba_2[1][1], complex(1.7,-1.78))

    def test_conj_matrix(self):
        prueba_1 = lb.conj_matrix(self.m1)
        self.assertAlmostEqual(prueba_1[0][0], complex(3.5,-2.8))
        self.assertAlmostEqual(prueba_1[0][1], complex(1.5,8.2))
        self.assertAlmostEqual(prueba_1[1][0], complex(1.5,-2.8))
        self.assertAlmostEqual(prueba_1[1][1], complex(2.7,-3.25))
        prueba_2 = lb.conj_matrix(self.m2)
        self.assertAlmostEqual(prueba_2[0][0], complex(-1.25,-5.15))
        self.assertAlmostEqual(prueba_2[0][1], complex(1.2,-3.70))
        self.assertAlmostEqual(prueba_2[1][0], complex(1.2,-2.78))
        self.assertAlmostEqual(prueba_2[1][1], complex(1.7,1.78))

    def test_adj_matrix(self):
        prueba_1 = lb.adj_matrix(self.m1)
        self.assertAlmostEqual(prueba_1[0][0], complex(3.5,-2.8))
        self.assertAlmostEqual(prueba_1[0][1], complex(1.5,-2.8))
        self.assertAlmostEqual(prueba_1[1][0], complex(1.5,8.2))
        self.assertAlmostEqual(prueba_1[1][1], complex(2.7,-3.25))
        prueba_2 = lb.adj_matrix(self.m2)
        self.assertAlmostEqual(prueba_2[0][0], complex(-1.25,-5.15))
        self.assertAlmostEqual(prueba_2[0][1], complex(1.2,-2.78))
        self.assertAlmostEqual(prueba_2[1][0], complex(1.2,-3.70))
        self.assertAlmostEqual(prueba_2[1][1], complex(1.7, 1.78))

    def test_act_matrix_vec(self):
        prueba_1 = lb.act_matrix_vec(self.m1,self.v1)
        self.assertAlmostEqual(prueba_1[0], complex(-59.31,-8.946))
        self.assertAlmostEqual(prueba_1[1], complex(30.2885,-3.165))
        prueba_2 = lb.act_matrix_vec(self.m2,self.v2)
        self.assertAlmostEqual(prueba_2[0], complex(-19.129,1.731))
        self.assertAlmostEqual(prueba_2[1], complex(1.312,-1.5124))

    def test_mul_matrix(self):
        prueba_1 = lb.mult_matrix(self.m1, self.m2)
        self.assertAlmostEqual(prueba_1[0][0], complex(5.801,8.855))
        self.assertAlmostEqual(prueba_1[0][1], complex(-18.206,-0.3))
        self.assertAlmostEqual(prueba_1[1][0], complex(-22.09,15.631))
        self.assertAlmostEqual(prueba_1[1][1], complex(1.815,9.629))
        prueba_2 = lb.mult_matrix(self.m2, self.m3)
        self.assertAlmostEqual(prueba_2[0][0], complex(0.7,41.87))
        self.assertAlmostEqual(prueba_2[0][1], complex(49.555,4.915))
        self.assertAlmostEqual(prueba_2[1][0], complex(-2.298,14.33))
        self.assertAlmostEqual(prueba_2[1][1], complex(15.376,-8.322))

    def test_prod_int_vec(self):
        prueba_1 = lb.prod_int_vec(self.v1,self.v2)
        self.assertAlmostEqual(prueba_1, complex(-21.8766, 41.611))
        prueba_2 = lb.prod_int_vec(self.v2,self.v3)
        self.assertAlmostEqual(prueba_2, complex(-21.28, -15.76))

    def test_norm_vec(self):
        prueba_1 = lb.norm_vec(self.v1)
        self.assertAlmostEqual(prueba_1, 9.43416133)
        prueba_2 = lb.norm_vec(self.v2)
        self.assertAlmostEqual(prueba_2, 5.240076335)

    def test_dist_vec(self):
        prueba_1 = lb.dist_vec(self.v1, self.v2)
        self.assertAlmostEqual(prueba_1, 12.65760641)
        prueba_2 = lb.dist_vec(self.v2, self.v3)
        self.assertAlmostEqual(prueba_2, 12.2343124)

    def test_prod_tens_vec(self):
        prueba_1 = lb.prod_tens_vec(self.v1, self.v2)
        self.assertAlmostEqual(prueba_1[0][0], complex(-12.175,4.52))
        self.assertAlmostEqual(prueba_1[0][1], complex(2.21,17.733))
        self.assertAlmostEqual(prueba_1[1][0], complex(17.421,19.3))
        self.assertAlmostEqual(prueba_1[1][1], complex(31.3484,-17.239))
        prueba_2 = lb.prod_tens_vec(self.v2, self.v3)
        self.assertAlmostEqual(prueba_2[0][0], complex(10.65,-3.72))
        self.assertAlmostEqual(prueba_2[0][1], complex(17.3,18.15))
        self.assertAlmostEqual(prueba_2[1][0], complex(-1.62,-15.438))
        self.assertAlmostEqual(prueba_2[1][1], complex(29.77,-17.44))

    def test_prod_tens_matrix(self):
        prueba_1 = lb.prod_tens_matrix(self.m1, self.m2)
        self.assertAlmostEqual(prueba_1[0][0], complex(-18.795,14.525))
        self.assertAlmostEqual(prueba_1[0][1], complex(-6.16,16.31))
        self.assertAlmostEqual(prueba_1[0][2], complex(40.355,17.975))
        self.assertAlmostEqual(prueba_1[0][3], complex(32.14,-4.29))
        self.assertAlmostEqual(prueba_1[1][0], complex(-3.584,13.09))
        self.assertAlmostEqual(prueba_1[1][1], complex(10.934,-1.47))
        self.assertAlmostEqual(prueba_1[1][2], complex(24.596,-5.67))
        self.assertAlmostEqual(prueba_1[1][3], complex(-12.046,-16.61))
        self.assertAlmostEqual(prueba_1[2][0], complex(-16.295,4.225))
        self.assertAlmostEqual(prueba_1[2][1], complex(-8.56,8.91))
        self.assertAlmostEqual(prueba_1[2][2], complex(-20.1125,9.8425))
        self.assertAlmostEqual(prueba_1[2][3], complex(-8.785,13.89))
        self.assertAlmostEqual(prueba_1[3][0], complex(-5.984,7.53))
        self.assertAlmostEqual(prueba_1[3][1], complex(7.534,2.09))
        self.assertAlmostEqual(prueba_1[3][2], complex(-5.795,11.406))
        self.assertAlmostEqual(prueba_1[3][3], complex(10.375,0.719))

        prueba_2 = lb.prod_tens_matrix(self.m2, self.m3)
        self.assertAlmostEqual(prueba_2[0][0], complex(-21.69,42.18))
        self.assertAlmostEqual(prueba_2[0][1], complex(40.855,15.915))
        self.assertAlmostEqual(prueba_2[0][2], complex(2.67,34.71))
        self.assertAlmostEqual(prueba_2[0][3], complex(31.66,-5.77))
        self.assertAlmostEqual(prueba_2[1][0], complex(26.2,15.63))
        self.assertAlmostEqual(prueba_2[1][1], complex(17.95,-6.55))
        self.assertAlmostEqual(prueba_2[1][2], complex(22.39,-0.31))
        self.assertAlmostEqual(prueba_2[1][3], complex(8.7,-11))
        self.assertAlmostEqual(prueba_2[2][0], complex(4.602,26.706))
        self.assertAlmostEqual(prueba_2[2][1], complex(24.116,-6.782))
        self.assertAlmostEqual(prueba_2[2][2], complex(18.528,-11.916))
        self.assertAlmostEqual(prueba_2[2][3], complex(-12.726,-15.898))
        self.assertAlmostEqual(prueba_2[3][0], complex(17.33,-1.874))
        self.assertAlmostEqual(prueba_2[3][1], complex(5.94,-9.16))
        self.assertAlmostEqual(prueba_2[3][2], complex(-6.9,-12.376))
        self.assertAlmostEqual(prueba_2[3][3], complex(-8.74,-1.54))

    m4 = np.array([[(complex(0,1)/math.sqrt(2)), (complex(0,-1)/math.sqrt(2))], [(complex(0,1)/math.sqrt(2)), (complex(0,1)/math.sqrt(2))]])
    m5 = np.array([[(complex(1,0)/math.sqrt(2)),(complex(1,0)/math.sqrt(2))],[(complex(1,0)/math.sqrt(2)),(complex(-1,0)/math.sqrt(2))]])
    def test_unit_matrix(self):
        prueba_1 = lb.unit_matrix(self.m4)
        self.assertEqual(prueba_1,True)
        prueba_2 = lb.unit_matrix(self.m1)
        self.assertEqual(prueba_2,False)

    def test_hermitian_matrix(self):
        prueba_1 = lb.hermitian_matrix(self.m1)
        self.assertEqual(prueba_1,False)
        prueba_2 = lb.hermitian_matrix(self.m5)
        self.assertEqual(prueba_2,True)


if __name__ == '__main__':
    unittest.main()