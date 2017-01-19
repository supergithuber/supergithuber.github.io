## iOS小技巧
---
### 1. **获取某个view所在的控制器**

```objc
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

### 2.**字符串反转**

* 第一种

```objc
- (NSString *)reverseWordsInString:(NSString *)str
{
    NSMutableString *newString = [[NSMutableString alloc] initWithCapacity:str.length];
    for (NSInteger i = str.length - 1; i >= 0 ; i --)
    {
        unichar ch = [str characterAtIndex:i];
        [newString appendFormat:@"%c", ch];
    }
    return newString;
}

```
* 第二种

```objc
- (NSString*)reverseWordsInString:(NSString*)str
{
    NSMutableString *reverString = [NSMutableString stringWithCapacity:str.length];
    [str enumerateSubstringsInRange:NSMakeRange(0, str.length) options:NSStringEnumerationReverse | NSStringEnumerationByComposedCharacterSequences  usingBlock:^(NSString *substring, NSRange substringRange, NSRange enclosingRange, BOOL *stop) {
    [reverString appendString:substring];
}];
    return reverString;
}

```

