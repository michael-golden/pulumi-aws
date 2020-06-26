// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Aws.Iot.Inputs
{

    public sealed class TopicRuleErrorActionSnsGetArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The message format of the message to publish. Accepted values are "JSON" and "RAW".
        /// </summary>
        [Input("messageFormat")]
        public Input<string>? MessageFormat { get; set; }

        /// <summary>
        /// The ARN of the IAM role that grants access.
        /// </summary>
        [Input("roleArn", required: true)]
        public Input<string> RoleArn { get; set; } = null!;

        /// <summary>
        /// The ARN of the SNS topic.
        /// </summary>
        [Input("targetArn", required: true)]
        public Input<string> TargetArn { get; set; } = null!;

        public TopicRuleErrorActionSnsGetArgs()
        {
        }
    }
}
