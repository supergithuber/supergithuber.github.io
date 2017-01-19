## iOS小技巧

1. 获取某个view所在的控制器

```objectivec
- (UIViewController *)viewController
{
	UIViewController *viewController = nil;
	UIResponder *next = self.nextResponder;
	while (next)
	{
		if ([next isKindOfClass:[UIViewController class]])
		{
			viewController = (UIViewController *)next;
			break;
		}
		next = next.nextResponder;
	}
	return viewController;
}

```

