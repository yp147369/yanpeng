#coding:gbk
"""
���ߣ���һ����
���ڣ�2021/11/30
"""

import random



# 0 - ʯͷ
# 1 - ʷ����
# 2 - ֽ
# 3 - ����
# 4 - ����

# ����Ϊ�����Ϸ����Ҫ�õ����Զ��庯��


def name_to_number(name):

    if name == "ʯͷ":
        return 0

    elif name == "ʷ����":
        return 1


    elif name == "��":
        return 1


    elif name == "����":
        return 3


    elif name=="����":
        return 4

    else:
        print ("Error:No Correct Name")








    """
    ����Ϸ�����Ӧ����ͬ������
    """







    # ʹ��if/elif/else��佫����Ϸ�����Ӧ����ͬ������
    # ��Ҫ���Ƿ��ؽ��


     #��дִ�д���,������ɺ�passɾ��


def number_to_name(number):


    if number == 0:
        return "ʯͷ"

    elif number == 1:
        return "ʷ����"

    elif number == 2:
        return "��"

    elif number == 3:
        return "����"

    elif number==4:
        return "����"

    else:
        print ("Error:No Crrect Name")




    """
    ������ (0, 1, 2, 3, or 4)��Ӧ����Ϸ�Ĳ�ͬ����
    """


    # ʹ��if/elif/else��佫��ͬ��������Ӧ����Ϸ�Ĳ�ͬ����
    # ��Ҫ���Ƿ��ؽ��

     #��дִ�д���,������ɺ�passɾ��


def rpsls(player_choice):


   choice_name =name_to_number(player_choice )
   comp_number=random.randrange(0,5)
   difference=(choice_name -comp_number)%5
   print ("����ѡ���ǣ�",player_choice)
   print ("���Ե�ѡ����:",number_to_name(comp_number))

   if difference  ==0:
    print("���ͼ��������һ����")

   elif difference ==1:
    print("��Ӯ��")

   elif difference ==2:
    print("��Ӯ��")

   elif difference==3:
    print("�����Ӯ��")

   else:
    print("�����Ӯ��")









"""
�û�����������һ��ѡ�񣬸���RPSLS��Ϸ��������Ļ�������Ӧ�Ľ��
"""










    # ���"-------- "���зָ�
    # ��ʾ�û�������ʾ���û�ͨ�����̽��Լ�����Ϸѡ��������룬�������player_choice

    # ����name_to_number()�������û�����Ϸѡ�����ת��Ϊ��Ӧ���������������player_choice_number

    # ����random.randrange()�Զ�����0-4֮��������������Ϊ��������ѡ�����Ϸ���󣬴������comp_number

    # ����number_to_name()����������������������ת��Ϊ��Ӧ����Ϸ����

    # ����Ļ����ʾ�����ѡ����������

    # ����if/elif/else ��䣬����RPSLS������û�ѡ��ͼ����ѡ������жϣ�������Ļ����ʾ�жϽ��

    # ����û��ͼ����ѡ��һ��������ʾ�����ͼ��������һ���ء�������û���ʤ������ʾ����Ӯ�ˡ�����֮����ʾ�������Ӯ�ˡ�

     #����������ʾ��дִ�д��룬������ɺ�ɾ����pass


# �Գ�����в���
print("��ӭʹ��RPSLS��Ϸ")
print("----------------")
print("���������ѡ��:")
choice_name=input()
rpsls(choice_name)




