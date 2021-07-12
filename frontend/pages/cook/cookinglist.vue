<template>
	<view>
		<view v-for="(item, index) in list" class="item" v-if="item.food_state==1">
			<u-row>
				<u-col span="3"><image :src="item.food_photourl" class="photo"></image></u-col>
				<u-col span="5.5">
					<text style="font-size: 60rpx;font-weight: bold;">{{item.food_name}}\n</text>
					<text class="info">桌号：{{item.order_table}}\n</text>
					<text class="info">{{item.order_time}}\n</text>
					<text class="info">订单编号：{{item.order_id}}</text>
				</u-col>
				<u-col span="3.5"><button class="button" @click="click(index)">完成</button></u-col>
			</u-row>
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
				list:[
					{
						food_name:"嫩牛五方",
						food_num:2,
						order_id:7942017948,
						order_table:2,
						order_time:"2021/7/11 15:45:20",
						food_state:1,
						food_photourl:"http://124.70.200.142:8080/img/food.png",
					},
					{
						food_name:"老牛五方",
						food_num:1,
						order_id:7942017948,
						order_table:2,
						order_time:"2021/7/11 15:45:20",
						food_state:1,
						food_photourl:"http://124.70.200.142:8080/img/food.png",
					},
					{
						food_name:"嫩羊五方",
						food_num:4,
						order_id:7942017948,
						order_table:2,
						order_time:"2021/7/11 15:45:20",
						food_state:1,
						food_photourl:"http://124.70.200.142:8080/img/food.png",
					},
					{
						food_name:"嫩牛七方",
						food_num:3,
						order_id:7942017948,
						order_table:2,
						order_time:"2021/7/11 15:45:20",
						food_state:1,
						food_photourl:"http://124.70.200.142:8080/img/food.png",
					},
					{
						food_name:"嫩牛五圆",
						food_num:2,
						order_id:7942017948,
						order_table:2,
						order_time:"2021/7/11 15:45:20",
						food_state:1,
						food_photourl:"http://124.70.200.142:8080/img/food.png",
					},
				]
			}
		},
		methods: {
			click(index){
				this.list[index].food_state=2;
			}
		},
		computed: {
			...mapGetters([
				'tabBarList'
			])
		},
	}
</script>

<style>
.photo{
	width: 160rpx;
	height:120rpx;
	margin-top: 40rpx;
	border-radius: 20rpx;
	border: #D8D8D8 thin solid;
}
.item{
	height:200rpx;
	
	border: solid thin #cbcbcb;
	border-radius: 20rpx;
	margin-left: 10rpx;
	margin-right: 10rpx;
	margin-top: 10rpx;
	box-shadow: 3px 3px 3px #d4d4d4;
}
.button{
	border-radius: 20rpx;
	background-color: #c51212;
	color:#F1F1F1;
	height:90rpx;
	width: 170rpx;
	line-height: 90rpx;
	font-weight: bold;
	margin-top: 40rpx;
}
.info{
	color: #888888;
}
</style>
