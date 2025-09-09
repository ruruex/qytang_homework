# 父类：基础订单
class Order:
    # 父类方法：计算金额（包含基础参数：商品价格、数量）
    def calculate(self, price, quantity):
        return price * quantity  # 基础逻辑：单价×数量


# 子类：优惠订单（继承基础订单）
class DiscountOrder(Order):
    # 重写父类方法：保留price和quantity参数，新增discount参数
    def calculate(self, price, quantity, discount=0.9):  # 新增折扣参数
        # 先调用父类的计算逻辑（复用基础功能）
        base_total = super().calculate(price, quantity)
        # 新增折扣计算（重写的部分）
        return base_total * discount


# 测试
base_order = Order()
print("基础订单金额：", base_order.calculate(100, 2))  # 100×2=200

discount_order = DiscountOrder()
# 既使用了父类的price、quantity参数，又用了子类新增的discount参数,discount为默认值0.9
print("优惠订单金额：", discount_order.calculate(100, 2))  # 200×0.9=180
# 额外定义折扣为0.8
print("自定义折扣订单金额：", discount_order.calculate(100, 2, 0.8))  # 200×0.8=160