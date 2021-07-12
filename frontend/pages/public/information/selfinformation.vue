<template>
	<view>
		<!-- 显示个人信息 -->
		<view class= "info" >
			<view style="display: flex;">
				<u-avatar :sex-icon="infodata.user_gender" show-sex :src="infodata.user_img" size= "200" style="margin-top: 50rpx;margin-left: 60rpx;"></u-avatar>
			</view>
			<view style="display: flex; flex-direction: column;">
				<view class="title" style="margin-top: 40rpx;">
					<text style="padding-left: 20rpx;font-weight: 600;">姓名：{{infodata.user_name}}</text>
				</view>
				<view class="title" style="margin-top: 20rpx;">
					<text style="padding-left: 20rpx;font-weight: 600;">工号：{{infodata.user_number}}</text>
				</view>
				<view class="title" style="margin-top: 20rpx;">
					<text style="padding-left: 20rpx;font-weight: 600;">职位：{{infodata.user_position}}</text>
				</view>
			</view>
		</view>
		<!-- cell组件 -->
		<view >
			<u-cell-group >
				<u-cell-item :title-style="tstyle" @click="set" style="height: 120rpx; font-weight: bold;" title="修改信息" border-top border-bottom></u-cell-item>
				<u-cell-item :title-style="tstyle" style="height: 120rpx;font-weight: bold;" title="设置" border-top border-bottom></u-cell-item>
				<u-cell-item :title-style="tstyle" style="height: 120rpx;font-weight: bold;" title="关于我们" border-top border-bottom></u-cell-item>
			</u-cell-group>
			<!-- 推出账户按钮 -->
			<u-button  style="margin-top: 50rpx; height: 100rpx; color: #FFFFFF; font-size: 50rpx; font-weight: 300;" type="error" @click="click">退 出 该 账 户</u-button>
		</view>
		<!-- 退出提示模态框 -->
		<u-modal @confirm="confirm" :content-style="constyle" :show-title=false confirm-color="#FA3534" show-cancel-button v-model="show" :content="content"></u-modal>
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
				// image: "../static/logo.png"
				infodata:{
					user_img: "http://124.70.200.142:8080/img/touxiang.jpg",
					user_name:"张鑫",
					user_number:20192997,
					user_position:"管理员",
					user_gender:"man"
				},
				tstyle:{ 
					'font-size': '35rpx',
				},
				show:false,
				content:"确定退出该账户", 
				constyle:{
					'font-size':'40rpx' 
				}
			}
		},
		methods: {
			set(index){
				console.log("修改信息");
				uni.navigateTo({
					url: "../setinfo/setinfo"
				})
			},
			click(){
				this.show=true
			},
			confirm(){
				console.log("确认退出")
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
.info{
	background-color: #F0AD4E;
	display: flex;
	width: 100%;
	height: 300rpx;
},
.title{
	margin-left: 50rpx;

	font-size: 40rpx;
	background-color: #F29100;
	height: 60rpx;
	border-radius: 15rpx;
	width: 380rpx;
	color: #3d3d3d;
}
</style>
