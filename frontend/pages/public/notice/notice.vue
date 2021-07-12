<template>
	<view>

		
		<view v-for="(item,index) in noticelist" style=" border-bottom: solid #acacac thin;" @click="click(index)">
			<u-col>
				<u-row span="1">
					<u-section v-if="item.priority=='普通'" :title=item.title sub-title="详情"
						style="margin-bottom: 10rpx; margin-top: 15rpx;" :tagText="item.priority" tagType="info">
					</u-section>
					<u-section v-if="item.priority=='重要'" :title=item.title sub-title="详情"
						style="margin-bottom: 10rpx; margin-top: 15rpx;" :tagText="item.priority" tagType="warning">
					</u-section>
					<u-section v-if="item.priority=='紧急'" :title=item.title sub-title="详情"
						style="margin-bottom: 10rpx; margin-top: 15rpx;" :tagText="item.priority" tagType="error">
					</u-section>
				</u-row>
				<u-row span="10">
					<text style="word-wrap: break-word; margin-left:15rpx;margin-bottom: 10rpx; margin-top: 20rpx; line-height: 45rpx;
					overflow:hidden; text-overflow:ellipsis;white-space: nowrap;">
						{{item.content}}
					</text>
				</u-row>
				<u-row span="1" style="margin-bottom: 15rpx; margin-left: 15rpx;">
					<text>{{item.user_name}}</text>
					<text space="emsp" style="color: #FFFFFF;">bla</text>
					<text style="color:#999999">{{item.notice_create_time}}</text>
				</u-row>
				<!-- 模态框 -->
				<u-modal v-model="show" :title="showlist.title">
					<view style="margin-left: 30rpx; margin-right: 30rpx;">
						<u-row style="margin-top:30rpx; margin-bottom:15rpx;">
							<!-- 公告信息 -->
							<!-- 公告 -->
							<u-col span="6">
								<!-- 发布者姓名 -->
								<u-row>
									<text style="font-size: 40rpx;">{{showlist.user_name}}</text>
								</u-row>
								<!-- 发布时间 -->
								<u-row>
									<text
										style="font-size: 20rpx; color:#999999;">{{showlist.notice_create_time}}</text>
								</u-row>
							</u-col>
						</u-row>
						<!-- 公告内容 -->
						<u-row span="12">
							<text
								style="margin-left: 0rpx;margin-right: 0rpx; font-size: 35rpx;">{{showlist.content}}</text>
						</u-row>
					</view>
				</u-modal>
			</u-col>
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
				noticelist: [{
						title: "我是大标题",
						content: "类快餐。牛肉蛋白质含量高，而脂肪含量低，所以味道鲜美，受人喜爱，享有“肉中骄子”的美称。",
						user_name: "发布人",
						notice_create_time: "2021/7/10 9:32:30",
						priority: "紧急",
					},
					{
						title: "我是大标题",
						content: "“嫩牛五方”是肯德基曾出的一款的卷饼类快餐。牛肉蛋白质含量高，而脂肪含量低，所以味道鲜美，受人喜爱，享有“肉中骄子”的美称。",
						user_name: "发布人",
						notice_create_time: "2021/7/10 9:32:30",
						priority: "重要",
					},
					{
						title: "我是大标题",
						content: "“嫩牛五方”是肯德基曾出的一款的卷饼类快餐。牛肉蛋白质含量高，而脂肪含量低，所以味道鲜美，受人喜爱，享有“肉中骄子”的美称。",
						user_name: "发布人",
						notice_create_time: "2021/7/10 9:32:30",
						priority: "普通",
					},
				],
				show: false,
				showlist: {
					title: "一个公告的标题一个公告的标题一个公告的标题",
					content: "一个公告的内容一个公告的内容一个公告的内容一个公告的内容一个公告的内容一个公告的内容一个公告的内容一个公告的内容一个公告的内容一个公告的内容一个公告的内容一个公告的内容一个公告的内容一个公告的内容一个公告的内容一个公告的内容一个公告的内容一个公告的内容一个公告的内容一个公告的内容一个公告的内容一个公告的内容一个公告的内容一个公告的内容一个公告的内容一个公告的内容一个公告的内容一个公告的内容一个公告的内容一个公告的内容一个公告的内容一个公告的内容一个公告的内容",
					user_name: "发布者",
					notice_create_time: "2021/7/10 11:10:49",
				},
			}
		},
		methods: {
			click(index) {
				this.showlist.title = this.noticelist[index].title;
				this.showlist.content = this.noticelist[index].content;
				this.showlist.user_name = this.noticelist[index].user_name;
				this.showlist.notice_create_time = this.noticelist[index].notice_create_time;
				this.show = true;
			},
			connect() {
				uni.request({
					url: 'api/announcement/fetch',
					method: 'GET',
					success: (res) => {
						//console.log(eval(res.data.data));
						this.noticelist = eval(res.data.data);
						console.log(res.data);
					}
				})
			}
		},
		computed: {
			...mapGetters([
				'tabBarList'
			])
		},
		onShow() {
			// this.connect();
		}
	}
</script>

<style scoped lang="scss">
</style>
