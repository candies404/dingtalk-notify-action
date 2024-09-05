# DingTalk Notification Action

<div align="center">
  <img src="https://img.alicdn.com/imgextra/i4/O1CN01RtfAks1Xa6qJFAekm_!!6000000002939-2-tps-128-128.png" width="100" height="100" alt="DingTalk Notification Icon">
</div>



这个 GitHub Action 用于发送各种类型的钉钉通知。支持文本、链接、Markdown、ActionCard 和 FeedCard 等多种消息类型。

## 功能特点

- 支持多种钉钉消息类型
- 使用钉钉的安全设置（加签）
- 简单易用，只需要提供少量必要参数
- 灵活的消息内容配置

## 使用方法

要使用这个 Action，你需要在你的 GitHub 仓库的 secrets 中设置以下两个值：

- `DINGTALK_TOKEN`：你的钉钉机器人的 access token
- `DINGTALK_SECRET`：你的钉钉机器人的加签密钥

然后，你可以在你的工作流程文件中使用这个 Action。以下是几种不同类型消息的使用示例：

### 文本消息

```yaml
- name: 发送钉钉文本通知
  uses: candies404/dingtalk-notify-action@v1.0.0
  with:
    dingtalk_token: ${{ secrets.DINGTALK_TOKEN }}
    dingtalk_secret: ${{ secrets.DINGTALK_SECRET }}
    msg_type: 'text'
    content: '{"content": "这是一条文本消息"}'
```

### 链接消息

```yaml
- name: 发送钉钉链接通知
  uses: candies404/dingtalk-notify-action@v1.0.0
  with:
    dingtalk_token: ${{ secrets.DINGTALK_TOKEN }}
    dingtalk_secret: ${{ secrets.DINGTALK_SECRET }}
    msg_type: 'link'
    content: '{"text": "这是一条链接消息", "title": "链接标题", "picUrl": "", "messageUrl": "https://www.example.com"}'
```

### Markdown 消息

```yaml
- name: 发送钉钉 Markdown 通知
  uses: candies404/dingtalk-notify-action@v1.0.0
  with:
    dingtalk_token: ${{ secrets.DINGTALK_TOKEN }}
    dingtalk_secret: ${{ secrets.DINGTALK_SECRET }}
    msg_type: 'markdown'
    content: '{"title": "Markdown 标题", "text": "### 标题\n- 项目1\n- 项目2"}'
```

### ActionCard 消息

```yaml
- name: 发送钉钉 ActionCard 通知
  uses: candies404/dingtalk-notify-action@v1.0.0
  with:
    dingtalk_token: ${{ secrets.DINGTALK_TOKEN }}
    dingtalk_secret: ${{ secrets.DINGTALK_SECRET }}
    msg_type: 'actionCard'
    content: '{"title": "ActionCard 标题", "text": "ActionCard 内容", "btnOrientation": "0", "singleTitle" : "阅读全文", "singleURL" : "https://www.example.com/"}'
```

### FeedCard 消息

```yaml
- name: 发送钉钉 FeedCard 通知
  uses: candies404/dingtalk-notify-action@v1.0.0
  with:
    dingtalk_token: ${{ secrets.DINGTALK_TOKEN }}
    dingtalk_secret: ${{ secrets.DINGTALK_SECRET }}
    msg_type: 'feedCard'
    content: '{"links": [{"title": "时代的火车向前开", "messageURL": "https://www.example.com/", "picURL": "https://img.example.com/image1.png"}]}'
```

## 输入参数

| 参数              | 描述                                                  | 是否必需 |
| ----------------- | ----------------------------------------------------- | -------- |
| `dingtalk_token`  | 钉钉机器人的 access token                             | 是       |
| `dingtalk_secret` | 钉钉机器人的加签密钥                                  | 是       |
| `msg_type`        | 消息类型 (text, link, markdown, actionCard, feedCard) | 是       |
| `content`         | 消息内容 (JSON 格式)                                  | 是       |

## 注意事项

1. 请确保您的钉钉机器人已正确配置，并且有发送消息的权限。
2. 消息内容必须是有效的 JSON 格式字符串。
3. 不同类型的消息有不同的内容格式要求，请参考[自定义机器人发送消息的消息类型](https://open.dingtalk.com/document/orgapp/custom-bot-send-message-type)。
4. 为了保护您的 access token 和 secret，请使用 GitHub 的 secrets 功能来存储这些敏感信息。

## 常见问题 (FAQ)

### 1. 为什么我的消息发送失败了？

请检查以下几点：

- **Access Token 和 Secret 是否正确**：确保您的 Access Token 和 Secret 输入无误。
- **消息内容格式是否正确**：请确认消息内容符合钉的[格式要求](https://open.dingtalk.com/document/orgapp/custom-bot-send-message-type)。
- **是否超出发送频率限制**：钉机器人有一定的[频率限制](https://open.dingtalk.com/document/orgapp/custom-bot-to-send-group-chat-messages#1b327a900b9xw)，请确保未超出限制。

### 2. 我可以在一个工作流中多次使用这个 Action 吗？

**是的**，您可以在同一个工作流中多次使用此 Action 来发送不同类型的消息。

## 贡献

欢迎提交 issues 和 pull requests 来改进这个 Action。如果您有任何建议或发现了 bug，请随时提出。

## 许可证

本项目采用 MIT 许可证。详情请见 [LICENSE](https://github.com/candies404/dingtalk-notify-action/blob/main/LICENSE) 文件。

## 联系方式

如果您有任何问题或需要支持，请通过以下方式联系我们：

- 在 GitHub 上提交 issue
- 发送邮件至：sugar404@qq.com

感谢您使用 DingTalk Notification Action！
