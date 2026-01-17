variable "env" {
  description = "Target environment (dev, staging)"
  type        = string
}

resource "aws_cloudwatch_event_rule" "nightly_stop" {
  name                = "nightly-stop-scheduler-${var.env}"
  description         = "Triggers Budget Police every night at 7 PM"
  schedule_expression = "cron(0 19 * * ? *)"
}

resource "aws_cloudwatch_event_target" "lambda_target" {
  rule      = aws_cloudwatch_event_rule.nightly_stop.name
  target_id = "BudgetPoliceLambda"
  arn       = var.lambda_arn
}

resource "aws_lambda_permission" "allow_cloudwatch" {
  statement_id  = "AllowExecutionFromCloudWatch"
  action        = "lambda:InvokeFunction"
  function_name = var.lambda_function_name
  principal     = "events.amazonaws.com"
  source_arn    = aws_cloudwatch_event_rule.nightly_stop.arn
}
