import sys
sys.path.append("C:/Users/HP/PycharmProjects/pythonProject/advance _python/package1")
#option1
import module1
import module2
module1.display()
module2.show()
#option-2
from module1 import*
from module2 import*
display()
show()