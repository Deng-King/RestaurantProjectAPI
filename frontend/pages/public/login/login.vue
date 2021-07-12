<template>
	<view class="content">
		<view>
			<u-row>
				<u-col span="0.5">
				</u-col>
				<u-col span="10">
					<text style="font-size: 40rpx; font-weight:bold">欢迎登录 \n</text>
					<text style="font-size: 60rpx;font-weight:500;">打工人餐饮系统</text>
				</u-col>
			</u-row>
		</view>
		<view class="item">
			<u-input  placeholder = "账号" v-model="userid" type="text" border inputAlign="left" />
		</view>
		
		<view class="item">
			<u-input placeholder = "密码" v-model="password" type="password" password-icon border />
		</view>
		
		<view>
			<!-- <u-button style="width: 50%; margin-top: 100rpx;color:#FFFFFF ; background-color: #F0AD4E;"  @click="click">登录</u-button> -->
			<u-button style="width: 50%; margin-top: 100rpx;" type="primary" @click="click">登录</u-button>
		</view>
		<u-button @click="admin">管理员</u-button>
		<u-button @click="cook">后厨</u-button>
		<u-button @click="waiter">服务员</u-button>
		<view>
			<u-toast ref="uToast" />
		</view>
	</view>
	
</template>

<script>
	import  tabBar from '../../../util/tabBar.js'
	export default {
		data() {
			return {
				userid:'',
				password:'',
				logintype:'',
				id:123,
				type:2
			}
		},
		
		methods: {
			click(){
				uni.request({
					url: "/api/login",
					method:"POST",
					data:{
						user_id : this.userid,
						user_password : this.password
					},
					success: (res) => { 
						if(res.statusCode!=200){
							this.$refs.uToast.show({
								title: '添加失败',
								type: 'error'
							});
						}else{
							console.log(res.data);
							this.id = '';
							this.name = '';
							this.$refs.uToast.show({
								title: '登陆成功',
								type: 'success'
							});
							uni.navigateTo({
								// url:"../selfinformation/selfinformation?user_id="res.data.data
								// url:"../second?userid="+this.userid+"&logintype="+this.logintype
							})
						}
					}

				})
			},
			admin(){
				this.$store.commit('tabBar/change',tabBar.admin)
				this.$store.commit('tabBar/changetype',1)
				this.$store.commit('tabBar/changeid',2222222)
				// console.log(this.$store.getters.tabBarList)
				uni.switchTab({
					url: '/pages/admin/notice/noticeadd'
				})
			},
			cook(){
				this.$store.commit('tabBar/change',tabBar.cook,1,1)
				this.$store.commit('tabBar/changetype',3)
				this.$store.commit('tabBar/changeid',2222222)
				// console.log(this.$store.getters.tabBarList)
				uni.switchTab({
					url: '/pages/public/notice/notice'
				})
			},
			waiter(){
				this.$store.commit('tabBar/change',tabBar.waiter,2,1)
				this.$store.commit('tabBar/changetype',2)
				this.$store.commit('tabBar/changeid',2222222)
				// console.log(this.$store.getters.tabBarList)
				uni.switchTab({
					url: '/pages/public/notice/notice'
				})
			}
		},
		onLoad() {

		}
	}
</script>

<style>
	.content {
		margin-top: 250rpx;
		/* display: flex; */
		flex-direction: column;
		align-items: center;
		justify-content: center;
	}

	.item {
		display: flex;
		margin: 40rpx 50rpx 30rpx 50rpx;
		background-color:#eef2fa;
		border-radius: 5rpx;
	}
/* 	.text-area {
		display: flex;
		justify-content: center;
	}

	.title {
		font-size: 36rpx;
		color: #8f8f94;
	} */
</style>
