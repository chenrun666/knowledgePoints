"""
数据库
"""

# 1， 数据库的设计能力
"""
    a，单表
    b，FK （一张表存储时，如果有重复出现的字段为了防止硬盘的浪费，所以做一个FK；去掉FK变成单表）
    c，M2M
    
    什么关系？单选的下拉框FK/radio；多选下拉框M2M / checkbox
    
    问题： 员工信息表，员工的当前工资。保留员工的所有调薪的记录
        思路一：
            员工表：
                id， name， salary
            调薪：
                id， price， time， 员工ID
        
        思路二：
            员工调薪表：
                id  uid  sid
"""

# 2， 基本SQL
"""
    分组：
        select depart_id, count(1), max(salary), min(age), sum(age) from user group by depart_id
        select depart_id, count(1), max(salary), min(age), sum(age) from user group by depart_id having count(1) > 5
    
    联表：
        数据：
            部门表：
                id  title
                1    销售
                2    运营
                3    IT
                
            用户表：
                id  name    部门id
                1   x1      1
                2   x1      2
                3   x1      3
                4   x1      1
                5   x1      2
    
        inner join / left join / right join
        
        select * from userinfo left join depart on userinfo_did = depart.id
        
        select * from depart left join userinfo on userinfo.did = depart.id
        
        select * from userinfo inner join depart on userinfo.did = depart.id
        
        select * from depart inner join userinfo on userinfo.did = depart.id    
"""

# 3, MySQL数据引擎： innodb， mysiam
"""
    a. 常见innodb，mysiam
    b. 区别：
        - inndb：
            - 支持事务（原子性， 一致性，隔离性，持久性）
            - 表锁
            - 行锁
        - mysiam
            - 不支持事务
            - 表锁
            - 全文索引
            - 速度快
            
            
    begin;
        select * from users where id=2 for update;
    commit;
    
    with trancation.automic:
        User.objects.filter().select_for_update()
    
    应用场景：商品数量计数。    
"""

# 4，索引
"""
    索引的作用：加速查找；约束
    种类：
        - 索引
        - 唯一索引 允许null，不重复
        - 主键索引 不允许null，不重复
        - 联合索引：多列组成一个索引
        - 联合唯一索引：多列组成一个索引。
        
        命中索引遵循最左前缀的原则
        
    补充：
        - 覆盖索引 当查找数据时候，在索引表中就能找到数据
            select name from user where name == "xxx"
        - 索引合并 使用多个单列索引进行查找
        
    为什么索引快？
        因为在索引结构中按照B+树进行存放数据
"""