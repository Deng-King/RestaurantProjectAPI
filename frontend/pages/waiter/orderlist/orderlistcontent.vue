<template>
	<view>
		<view v-for="(item, index) in list.order_list" class="item">
			<u-row>
				<u-col span="3"><image :src="item.food_photourl" class="photo"></image></u-col>
				<u-col span="3"><text class="name">{{item.food_name}}</text></u-col>
				<u-col span="3">
					<u-row><text class="info">单价：{{item.food_price}}</text></u-row>
					<u-row><text class="info">数量：{{item.food_num}}</text></u-row>
				</u-col>
				<u-col span="3">
					<u-tag v-if="item.food_state==0" text="正在烹饪" type="warning"  shape="circle" :closeable="false" mode="dark"/>
					<u-tag v-if="item.food_state==1" text="等待上菜" type="error"  shape="circle" :closeable="false" mode="dark"/>
					<u-tag v-if="item.food_state==2" text="已上菜" type="success"  shape="circle" :closeable="false" mode="dark"/>
				</u-col>
			</u-row>
		</view>
		<u-row style="float:right; margin-right: 30rpx;">
			<text class="total">共计：{{list.order_total}}元</text>
		</u-row>
		<u-divider style="margin-top: 40rpx;">订单信息</u-divider>
		<view>
			<text class="orderinfo">桌号：{{list.order_table}}\n</text>
			<text class="orderinfo">下单时间：{{list.order_time}}\n</text>
			<text class="orderinfo">服务人员：{{list.order_name}}\n</text>
		</view>
		
	</view>
</template>

<script>
	export default {
		data() {
			return {
				list:{
					order_name:"Chloe",
					order_id:49104141311,
					order_time:"2021/7/11 14:28:30",
					order_list:[
						{
							food_id:1,
							food_num:2,
							food_name:"嫩牛五方",
							food_state:0,
							food_price:4,
							food_photourl:"http://124.70.200.142:8080/img/food.png",
						},
						{
							food_id:1,
							food_num:2,
							food_name:"嫩牛六方",
							food_state:1,
							food_price:25,
							food_photourl:"http://124.70.200.142:8080/img/food.png",
						},
						{
							food_id:1,
							food_num:1,
							food_name:"嫩牛五圆",
							food_state:2,
							food_price:43,
							food_photourl:"http://124.70.200.142:8080/img/food.png",
						},
						{
							food_id:1,
							food_num:22,
							food_name:"嫩羊五方",
							food_state:1,
							food_price:41,
							food_photourl:"http://124.70.200.142:8080/img/food.png",
						},
						{
							food_id:1,
							food_num:25,
							food_name:"老牛五方",
							food_state:0,
							food_price:2,
							food_photourl:"http://124.70.200.142:8080/img/food.png",
						},
					],
					order_table:1,
					order_total:1000,
				}
			}
		},
		methods: {
			
		}
	}
</script>

<style>
.pay{
	font-weight: bold;
	color:#c2c1c5;
	font-size:50rpx;
}
.table{
	font-size:60rpx;
	margin-left: 20rpx;
}
.item{
	height:175rpx;
	
	border: solid thin #cbcbcb;
	border-radius: 20rpx;
	margin-left: 10rpx;
	margin-right: 10rpx;
	margin-top: 15rpx;
	box-shadow: 3px 3px 3px #d4d4d4;
	background-color: #ffffff;
}
.photo{
	width: 160rpx;
	height:120rpx;
	line-height: 120rpx;
	margin-top: 30rpx;
	border-radius: 20rpx;
	border: #D8D8D8 thin solid;
}
.name{
	font-size: 33rpx;
	font-weight: bold;
}
.info{
	color:#939393;
}
.total{
	font-size: 70rpx;
	margin-top: 20rpx;
	margin-bottom: 20rpx;
}
.orderinfo{
	margin-left: 30rpx;
	margin-top: 5rpx;
	margin-bottom: 5rpx;
	color:#888888;
}
</style>
