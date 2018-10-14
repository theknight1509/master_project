#!/usr/bin/python2.7

import math as m

def num2str(num):
    if type(num) is float:
        return "%2.4f"%num
    elif type(num) is type(None):
        return "None"
    else:
        return "undist."

class Value(object):
    def __init__(self, value=None, abs_unc=None, rel_unc=None, debug=False):
        if (abs_unc is not None) and (rel_unc is not None):
            raise ValueError("Only one uncertainty variable can be given at instantiation!")
        
        self._value = value
        self._abs_unc = abs_unc #Absolute uncertainty
        self._rel_unc = rel_unc #Relative Uncertainty
        self.debug = debug

        self.calculate()
        return

    def get_value(self): return self._value
    def get_abs_unc(self): return self._abs_unc
    def get_rel_unc(self): return self._rel_unc

    def set_value(self, value):
        self._value = value
        self.calculate()
        return
    def set_abs_unc(self, abs_unc):
        self._abs_unc = abs_unc
        self.calculate()
        return
    def set_rel_unc(self, rel_unc):
        self._rel_unc = rel_unc
        self.calculate()
        return

    def __str__(self):
        return "Value( %s +/- %s +/- %s%% )"%(num2str(self._value), num2str(self._abs_unc), num2str(self._rel_unc))
    
    def get_status(self):
        """
        code: 0 - no variables present
        code: 1 - only 'value' present
        code: 2 - 'value' and 'abs_unc' present
        code: 3 - 'value' and 'rel_unc' present
        code: 4 - no 'value' present
        code: 10 - all variables present
        """
        val_bool = (self._value is not None)
        abs_bool = (self._abs_unc is not None)
        rel_bool = (self._rel_unc is not None)
        if val_bool:
            if abs_bool:
                if rel_bool: return 10
                else: return 2
            else:
                if rel_bool: return 3
                else: return 1
        else: return 4

    def calculate(self):
        status = self.get_status()
        if self.debug == True:
            print "status = ", status
        if status in [0, 1, 4, 10]: pass
        elif status == 2: self.calculate_rel_unc()
        elif status == 3: self.calculate_abs_unc()
        else: print "Warning: status-code not found!"
        return

    def calculate_rel_unc(self):
        self._rel_unc = self._abs_unc / float(self._value)
        return

    def calculate_abs_unc(self):
        self._abs_unc = self._rel_unc * float(self._value)
        return


def calc_f_form_rel(f_now, half_life, sos_age):
    if (type(f_now) is not Value) or (type(half_life) is not Value) or (type(sos_age) is not Value):
        raise ValueError("Warning: Input arguments must be Value-types!")

    sos_age__halflife = sos_age.get_value()/half_life.get_value()
    exponential = m.exp(-2.0*m.log(2.0)*sos_age__halflife)
    parenthesis = ((sos_age__halflife)**2 * half_life.get_rel_unc()**2) - (sos_age.get_rel_unc()**2)
    bracket = f_now.get_rel_unc()**2 + (f_now.get_value() + 1)**2*(m.log(2.0)/half_life.get_value())**2*parenthesis

    print "calculated (d f_form/f_form)^2 = ", exponential*bracket
    return m.sqrt(exponential*bracket)

half_life_value = Value(value=41.577, abs_unc=0.12) #Unit=Gyr
sos_age_value = Value(value=4.5682, abs_unc=0.4e-3) #Unit=Gyr
correct_f_now_value = Value(value=0.226, abs_unc=5.79e-3) #Unit=1
wrong_f_now_value = Value(value=0.226, abs_unc=5.79e-2) #Unit=1

wrong_f_form_rel = calc_f_form_rel(f_now=wrong_f_now_value, half_life=half_life_value, sos_age=sos_age_value)
wrong_f_form_value = Value(value=0.136, rel_unc=wrong_f_form_rel)

correct_f_form_rel = calc_f_form_rel(f_now=correct_f_now_value, half_life=half_life_value, sos_age=sos_age_value)
correct_f_form_value = Value(value=0.136, rel_unc=correct_f_form_rel)

print "Wrong calculated value: ", wrong_f_form_value
print "Correct calculated value: ", correct_f_form_value
