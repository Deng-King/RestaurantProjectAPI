<template>
	<view>
		<!-- cell组件 -->
		<u-cell-group>
			<u-cell-item @click="set" style="height: 160rpx;" :title-style="tstyle" title="头像" border-top border-bottom>
				<u-avatar size="110" :src="infodata.user_img" style="margin-top: 20rpx;margin-right: 20rpx;"></u-avatar>
			</u-cell-item>
			
			<u-cell-item hover-class='none' :arrow="false" :value-style="vstyle" :title-style="tstyle" title="姓名" style="height: 120rpx;">{{infodata.user_name}}</u-cell-item>
			<u-cell-item hover-class='none' :arrow="false" :value-style="vstyle" :title-style="tstyle" title="性别" style="height: 120rpx;">{{infodata.user_gender==="man"?"男":"女"}}</u-cell-item>
			<u-cell-item hover-class='none' :arrow="false" :value-style="vstyle" :title-style="tstyle" title="工号" style="height: 120rpx;">{{infodata.user_number}}</u-cell-item>
			<u-cell-item hover-class='none' :arrow="false" :value-style="vstyle" :title-style="tstyle" title="职位" style="height: 120rpx;">{{infodata.user_position}}</u-cell-item>
			<u-cell-item @click="pwdclick" :arrow="true"  :value-style="vstyle" :title-style="tstyle" title="更改密码" style="height: 120rpx;"></u-cell-item>
		</u-cell-group>
		<!-- 修改密码模态框 -->
		<u-modal  v-model="pwdshow"  @confirm="confirm" ref="uModal"  title="修改密码" :show-cancel-button="true">
			<view class="input_item">
				<u-input height="80" placeholder = "输入新密码" v-model="new_pwd" type='text' :border="true"/>
			</view>
		</u-modal>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				infodata:{
					user_img: "http://124.70.200.142:8080/img/touxiang.jpg",
					user_gender:"man",
					user_name:"张鑫",
					user_number:20192997,
					user_position:"管理员"
				},
				tstyle:{
					'font-size': '40rpx',
					'font-weight': 'bold'
				},
				vstyle:{
					'font-size': '40rpx',
					'font-weight': 'bold',
					'margin-right': '25rpx'
				},
				pwdshow: false,
				new_pwd:''
			}
		},
		methods: {
			confirm(){
				console.log("确定修改密码")
			},
			pwdclick(){
				console.log("更改密码"),
				this.pwdshow=true
			},
			set(){
				console.log("设置头像")
			}
		}
	}
</script>

<style>
.input_item {
		margin-top: 20rpx;
		margin-left: 20rpx;
		margin-right: 20rpx;
		margin-bottom: 30rpx;
		display: flex;
		padding: 10rpx;
		border-color:#999999;
	}
</style>
