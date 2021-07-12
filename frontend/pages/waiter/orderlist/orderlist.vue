<template>
	<view>
		<!-- 标签 -->
		<u-tabs v-if="true" bg-color="#fafafa" :bold="true" :list="options" @change="change" :current="current"
				:is-scroll="true" :gutter="gutter" :bar-width="barwidth" :font-size="fontsize"
				style="margin-left: 100rpx; margin-right: 100rpx;"></u-tabs>
		
		<!-- 订单页 -->
		<view v-if="current==0">
			<view v-for="(item, index) in orderlist" class="item" v-if="item.order_state==0">
				<u-row @click="click1()">
					<u-col span="7"><text class="table"> 桌号：{{item.order_table}}</text></u-col>
					<u-col span="5" style="text-align: center;"><text v-if="item.order_state==0" class="pay">未付款</text>
					</u-col>
				</u-row>
				<u-row style="margin-top: 10rpx;">
					<u-col span="7" @click="click1()"><text class="content">查看详情</text></u-col>
					<u-col span="5"><button type="default" class="button1" @click="click(index)"> 结单</button></u-col>
				</u-row>
			</view>
		</view>
		<!-- 上菜页 -->
		<view v-if="current==1">
			<view v-for="(item, index) in sclist" class="item" v-if="item.food_state==1">
				<u-row>
					<u-col span="2.5">
						<image :src="item.food_photourl" class="photo"></image>
					</u-col>
					<u-col span="4.5">
						<u-row><text class="name">{{item.food_name}}</text></u-row>
						<u-row><text>数量:{{item.food_num}}</text></u-row>
						<u-row>订单号:{{item.order_id}}</u-row>
					</u-col>
					<u-col span="4">
						<u-row><text style="font-size: 50rpx; font-weight: bold;">桌号:{{item.order_table}}</text></u-row>
						<u-row><button class="button2" @click="click2(index)">等待上菜</button></u-row>
					</u-col>
				</u-row>
			</view>
		</view>
		<u-tabbar
			:list="tabBarList"
			active-color="#5098FF"
			inactive-color="#909399"
			:border-top= false
			bg-color = "#F8F8F8"
		></u-tabbar>
	</view>
</template>

<script>
	import { mapGetters } from 'vuex'
	export default {
		data() {
			return {
				orderlist: [{
						order_id: 123,
						order_table: 1,
						order_state: 0,
						order_total: 100,
						order_create_time: '2021/7/11 11:35',
					},
					{
						order_id: 123,
						order_table: 2,
						order_state: 0,
						order_total: 100,
						order_create_time: '2021/7/11 11:35',
					},
					{
						order_id: 123,
						order_table: 7,
						order_state: 0,
						order_total: 100,
						order_create_time: '2021/7/11 11:35',
					},
					{
						order_id: 123,
						order_table: 3,
						order_state: 0,
						order_total: 100,
						order_create_time: '2021/7/11 11:35',
					},
					{
						order_id: 123,
						order_table: 4,
						order_state: 0,
						order_total: 100,
						order_create_time: '2021/7/11 11:35',
					},
					{
						order_id: 123,
						order_table: 5,
						order_state: 0,
						order_total: 100,
						order_create_time: '2021/7/11 11:35',
					},
					{
						order_id: 123,
						order_table: 6,
						order_state: 0,
						order_total: 100,
						order_create_time: '2021/7/11 11:35',
					},
				],				
				sclist:[
					{
						food_name:"嫩牛五方",
						food_num:2,
						order_id:739340180,
						order_table:2,
						food_state:1,
						food_photourl:"http://124.70.200.142:8080/img/food.png",
					},
					{
						food_name:"嫩牛六方",
						food_num:2,
						order_id:7390180,
						order_table:2,
						food_state:1,
						food_photourl:"http://124.70.200.142:8080/img/food.png",
					},
					{
						food_name:"老牛五方",
						food_num:2,
						order_id:7390180,
						order_table:2,
						food_state:1,
						food_photourl:"http://124.70.200.142:8080/img/food.png",
					},
					{
						food_name:"嫩羊五方",
						food_num:2,
						order_id:7390180,
						order_table:2,
						food_state:1,
						food_photourl:"http://124.70.200.142:8080/img/food.png",
					},
					{
						food_name:"嫩牛五圆",
						food_num:2,
						order_id:7390180,
						order_table:2,
						food_state:1,
						food_photourl:"http://124.70.200.142:8080/img/food.png",
					},
				],
				options: [{
						name: "订单",
					},
					{
						name: "上菜",
					}
				],
				// 与tabs相关的参数
				current: 0,
				gutter:90,
				barwidth:90,
				fontsize:40,
			}
		},
		methods: {
			click(index) {
				this.orderlist[index].order_state = 1;
			},
			click1(index) {
				uni.navigateTo({
					url: 'orderorderlistcontent/orderorderlistcontent'
				})
			},
			click2(index){
				this.sclist[index].food_state=2;
			},
			change(index) {
				this.current = index;
			}
		},
		computed: {
			...mapGetters([
				'tabBarList'
			])
		}
	}
</script>

<style>
	.button1 {
		border-radius: 40rpx;
		background-color: #fa3534;
		color: #F1F1F1;
		height: 60rpx;
		line-height: 60rpx;
		margin-left: 25rpx;
		margin-right: 25rpx;
		font-weight: bold;
	}
	.button2{
		border-radius: 20rpx;
		height: 80rpx;
		line-height: 80rpx;
		border: #f29100 solid thin;
		background-color: #ff9900;
		color: #FFFFFF;
	}

	.pay {
		font-weight: bold;
		color: #c2c1c5;
		font-size: 50rpx;
	}

	.table {
		font-size: 60rpx;
		margin-left: 20rpx;
	}

	.item {
		height: 175rpx;
		border: solid thin #cbcbcb;
		border-radius: 20rpx;
		margin-left: 10rpx;
		margin-right: 10rpx;
		margin-top: 15rpx;
		box-shadow: 3px 3px 3px #d4d4d4;

	}

	.content {
		margin-left: 20rpx;
		color: #8b8b8b;
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
</style>
