//()��ȣ ���߱�

#include <stdio.h>
#include <string.h>

int main() {

	int i, j, n, size, num;
	char s[50];

	scanf("%d\n", &n);

	for (i = 0; i < n; i++) {
		num = 0;
		scanf("%s", s);
		
		size = strlen(s);
;
		for (j = 0; j < size; j++) {
			if (s[j] == '(') {
				num ++;
			}
			else if (s[j] == ')' && num > 0) {	//else if ���̽� �ΰ� �����ִ°� ! (�ѹ� Ʋ��)
				num--;
			}
			else if (s[j] == ')' && num <= 0) {
				num--;
				break;
			}
		}

		if (num == 0) {
			printf("YES\n");
		}
		else {
			printf("NO\n");
		}

	}

}